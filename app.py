import os
import io
import json
import sqlite3
import zipfile
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session, send_file
from database import get_db, init_db

app = Flask(__name__)
app.secret_key = 'priyhire-secret-key-production-ready'

# Helper to ensure database is initialized
@app.before_request
def ensure_db():
    if not hasattr(app, '_db_checked'):
        init_db()
        app._db_checked = True

# Helper to get or generate user session
def get_user_session():
    if 'user_session_id' not in session:
        session['user_session_id'] = 'user_' + os.urandom(8).hex()
    return session['user_session_id']

# ----------------- HOME ROUTE -----------------
@app.route('/')
def home():
    user_sess = get_user_session()
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Statistics
        cursor.execute("SELECT COUNT(*) FROM jobs")
        total_jobs = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM companies")
        total_companies = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM dsa_problems")
        total_dsa = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM applications")
        total_applications = cursor.fetchone()[0]
        
        # User DSA solved count
        cursor.execute("SELECT COUNT(*) FROM dsa_progress WHERE user_session = ? AND is_solved = 1", (user_sess,))
        user_dsa_solved = cursor.fetchone()[0]
        
        # Featured Jobs
        cursor.execute("SELECT * FROM jobs ORDER BY is_featured DESC, created_at DESC LIMIT 6")
        featured_jobs = cursor.fetchall()
        
        # Top Companies
        cursor.execute("SELECT * FROM companies LIMIT 6")
        featured_companies = cursor.fetchall()
        
        # Featured Prep Modules
        cursor.execute("SELECT * FROM prep_modules ORDER BY order_index ASC LIMIT 4")
        featured_prep = cursor.fetchall()
        
        # Sample DSA Problems
        cursor.execute("SELECT * FROM dsa_problems ORDER BY order_index ASC LIMIT 5")
        sample_dsa = cursor.fetchall()

    return render_template(
        'index.html',
        total_jobs=total_jobs,
        total_companies=total_companies,
        total_dsa=total_dsa,
        total_applications=total_applications,
        user_dsa_solved=user_dsa_solved,
        featured_jobs=featured_jobs,
        featured_companies=featured_companies,
        featured_prep=featured_prep,
        sample_dsa=sample_dsa
    )

# ----------------- JOB PORTAL ROUTES -----------------
@app.route('/jobs')
def jobs_list():
    keyword = request.args.get('q', '').strip()
    category = request.args.get('category', '').strip()
    job_type = request.args.get('job_type', '').strip()
    experience = request.args.get('experience', '').strip()
    location = request.args.get('location', '').strip()
    
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []
    
    if keyword:
        query += " AND (title LIKE ? OR company LIKE ? OR skills LIKE ? OR description LIKE ?)"
        term = f"%{keyword}%"
        params.extend([term, term, term, term])
    
    if category:
        query += " AND category = ?"
        params.append(category)
        
    if job_type:
        query += " AND job_type = ?"
        params.append(job_type)
        
    if experience:
        query += " AND experience_level = ?"
        params.append(experience)
        
    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
        
    query += " ORDER BY is_featured DESC, created_at DESC"
    
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        jobs = cursor.fetchall()
        
        # Get distinct categories for filters
        cursor.execute("SELECT DISTINCT category FROM jobs ORDER BY category")
        categories = [row[0] for row in cursor.fetchall()]
        
        # Get distinct locations
        cursor.execute("SELECT DISTINCT job_type FROM jobs ORDER BY job_type")
        job_types = [row[0] for row in cursor.fetchall()]

        # Get saved job IDs for this user
        user_sess = get_user_session()
        cursor.execute("SELECT job_id FROM saved_jobs WHERE user_session = ?", (user_sess,))
        saved_job_ids = {row[0] for row in cursor.fetchall()}

    return render_template(
        'jobs/list.html',
        jobs=jobs,
        categories=categories,
        job_types=job_types,
        saved_job_ids=saved_job_ids,
        selected_category=category,
        selected_job_type=job_type,
        selected_experience=experience,
        keyword=keyword,
        location=location
    )

@app.route('/jobs/<int:job_id>')
def job_detail(job_id):
    user_sess = get_user_session()
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM jobs WHERE id = ?", (job_id,))
        job = cursor.fetchone()
        if not job:
            flash("Job posting not found", "error")
            return redirect(url_for('jobs_list'))
            
        # Check if saved
        cursor.execute("SELECT 1 FROM saved_jobs WHERE job_id = ? AND user_session = ?", (job_id, user_sess))
        is_saved = cursor.fetchone() is not None
        
        # Check if user already applied
        cursor.execute("SELECT * FROM applications WHERE job_id = ? ORDER BY applied_at DESC LIMIT 1", (job_id,))
        previous_app = cursor.fetchone()
        
        # Related jobs
        cursor.execute("SELECT * FROM jobs WHERE category = ? AND id != ? LIMIT 3", (job['category'], job_id))
        related_jobs = cursor.fetchall()

    return render_template('jobs/detail.html', job=job, is_saved=is_saved, previous_app=previous_app, related_jobs=related_jobs)

@app.route('/post-job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form.get('title')
        company = request.form.get('company')
        company_logo = request.form.get('company_logo') or "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=120&h=120&q=80"
        location = request.form.get('location')
        job_type = request.form.get('job_type')
        experience_level = request.form.get('experience_level')
        salary_range = request.form.get('salary_range')
        category = request.form.get('category')
        description = request.form.get('description')
        requirements = request.form.get('requirements')
        skills = request.form.get('skills')
        openings = int(request.form.get('openings', 1))
        deadline = request.form.get('deadline')
        company_website = request.form.get('company_website')
        
        with get_db() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO jobs (
                    title, company, company_logo, location, job_type, experience_level,
                    salary_range, category, description, requirements, skills, openings,
                    deadline, company_website, is_featured
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
            ''', (title, company, company_logo, location, job_type, experience_level,
                  salary_range, category, description, requirements, skills, openings,
                  deadline, company_website))
            new_id = cursor.lastrowid
            
        flash("Job posting published successfully! It is now live in the job portal.", "success")
        return redirect(url_for('job_detail', job_id=new_id))

    return render_template('jobs/post.html')

@app.route('/api/jobs/apply', methods=['POST'])
def api_apply_job():
    data = request.get_json() if request.is_json else request.form
    job_id = data.get('job_id')
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    resume_link = data.get('resume_link')
    portfolio_link = data.get('portfolio_link', '')
    experience_years = data.get('experience_years', 'Fresher')
    cover_note = data.get('cover_note', '')
    
    if not job_id or not name or not email or not phone:
        return jsonify({'success': False, 'message': 'Please fill all required fields.'}), 400
        
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO applications (
                job_id, applicant_name, applicant_email, applicant_phone,
                resume_link, portfolio_link, experience_years, cover_note, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'Under Review')
        ''', (job_id, name, email, phone, resume_link, portfolio_link, experience_years, cover_note))
        
    return jsonify({
        'success': True,
        'message': 'Application submitted successfully! Your application is now Under Review.'
    })

@app.route('/api/jobs/save', methods=['POST'])
def api_toggle_save_job():
    data = request.get_json() or {}
    job_id = data.get('job_id')
    user_sess = get_user_session()
    
    if not job_id:
        return jsonify({'success': False, 'message': 'Missing job_id'}), 400
        
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM saved_jobs WHERE job_id = ? AND user_session = ?", (job_id, user_sess))
        existing = cursor.fetchone()
        
        if existing:
            cursor.execute("DELETE FROM saved_jobs WHERE id = ?", (existing[0],))
            saved = False
        else:
            cursor.execute("INSERT INTO saved_jobs (job_id, user_session) VALUES (?, ?)", (job_id, user_sess))
            saved = True
            
    return jsonify({'success': True, 'saved': saved})

# ----------------- PREPARATION HUB ROUTES -----------------
@app.route('/prep')
def prep_index():
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Modules count by category
        cursor.execute("SELECT category, COUNT(*) FROM prep_modules GROUP BY category")
        counts = dict(cursor.fetchall())
        
        # Quiz count
        cursor.execute("SELECT category, COUNT(*) FROM quiz_questions GROUP BY category")
        quiz_counts = dict(cursor.fetchall())
        
        # Recent modules
        cursor.execute("SELECT * FROM prep_modules ORDER BY order_index ASC")
        all_modules = cursor.fetchall()

    return render_template(
        'prep/index.html',
        counts=counts,
        quiz_counts=quiz_counts,
        modules=all_modules
    )

@app.route('/prep/aptitude')
def prep_aptitude():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prep_modules WHERE category = 'aptitude' ORDER BY order_index ASC")
        modules = cursor.fetchall()
        
        cursor.execute("SELECT * FROM quiz_questions WHERE category = 'aptitude'")
        quizzes = cursor.fetchall()
        
    return render_template('prep/aptitude.html', modules=modules, quizzes=quizzes)

@app.route('/prep/technical')
def prep_technical():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prep_modules WHERE category = 'technical' ORDER BY order_index ASC")
        modules = cursor.fetchall()
        
        cursor.execute("SELECT * FROM quiz_questions WHERE category = 'technical'")
        quizzes = cursor.fetchall()
        
    return render_template('prep/technical.html', modules=modules, quizzes=quizzes)

@app.route('/prep/hr')
def prep_hr():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prep_modules WHERE category = 'hr' ORDER BY order_index ASC")
        modules = cursor.fetchall()
        
    return render_template('prep/hr.html', modules=modules)

@app.route('/prep/dsa-notes')
def prep_dsa_notes():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prep_modules WHERE category = 'dsa' ORDER BY order_index ASC")
        modules = cursor.fetchall()
        
    return render_template('prep/dsa_notes.html', modules=modules)

@app.route('/prep/module/<slug>')
def prep_module_detail(slug):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prep_modules WHERE slug = ?", (slug,))
        module = cursor.fetchone()
        if not module:
            flash("Study module not found", "error")
            return redirect(url_for('prep_index'))
            
        cursor.execute("SELECT * FROM prep_modules WHERE category = ? AND id != ? LIMIT 3", (module['category'], module['id']))
        related = cursor.fetchall()
        
    return render_template('prep/module_detail.html', module=module, related=related)

@app.route('/api/quiz/questions/<category>')
def api_get_quiz_questions(category):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, category, subtopic, question_text, option_a, option_b, option_c, option_d, difficulty FROM quiz_questions WHERE category = ?", (category,))
        rows = cursor.fetchall()
        questions = [dict(row) for row in rows]
    return jsonify(questions)

@app.route('/api/quiz/check', methods=['POST'])
def api_check_quiz_answer():
    data = request.get_json() or {}
    question_id = data.get('question_id')
    user_answer = data.get('selected_option', '').strip().upper()
    
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT correct_option, explanation FROM quiz_questions WHERE id = ?", (question_id,))
        row = cursor.fetchone()
        
    if not row:
        return jsonify({'success': False, 'message': 'Question not found'}), 404
        
    correct_option = row['correct_option']
    is_correct = (user_answer == correct_option)
    
    return jsonify({
        'success': True,
        'is_correct': is_correct,
        'correct_option': correct_option,
        'explanation': row['explanation']
    })

# ----------------- COMPANIES HIRING PROCESS ROUTES -----------------
@app.route('/companies')
def companies_list():
    tier = request.args.get('tier', '').strip()
    keyword = request.args.get('q', '').strip()
    
    query = "SELECT * FROM companies WHERE 1=1"
    params = []
    
    if tier:
        query += " AND tier LIKE ?"
        params.append(f"%{tier}%")
        
    if keyword:
        query += " AND (name LIKE ? OR industry LIKE ? OR overview LIKE ?)"
        term = f"%{keyword}%"
        params.extend([term, term, term])
        
    query += " ORDER BY name ASC"
    
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        companies = cursor.fetchall()
        
    return render_template(
        'companies/list.html',
        companies=companies,
        selected_tier=tier,
        keyword=keyword
    )

@app.route('/companies/<slug>')
def company_detail(slug):
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM companies WHERE slug = ?", (slug,))
        company = cursor.fetchone()
        if not company:
            flash("Company not found", "error")
            return redirect(url_for('companies_list'))
            
        # Parse JSON structured fields
        eligibility = json.loads(company['eligibility_criteria']) if company['eligibility_criteria'] else {}
        exam_pattern = json.loads(company['exam_pattern']) if company['exam_pattern'] else {}
        syllabus = json.loads(company['syllabus']) if company['syllabus'] else {}
        selection_process = json.loads(company['selection_process']) if company['selection_process'] else []
        
        # Check active jobs for this company
        cursor.execute("SELECT * FROM jobs WHERE company LIKE ?", (f"%{company['name']}%",))
        active_jobs = cursor.fetchall()

    return render_template(
        'companies/detail.html',
        company=company,
        eligibility=eligibility,
        exam_pattern=exam_pattern,
        syllabus=syllabus,
        selection_process=selection_process,
        active_jobs=active_jobs
    )

# ----------------- DEDICATED DSA SHEET ROUTES -----------------
@app.route('/dsa-sheet')
def dsa_sheet():
    user_sess = get_user_session()
    topic = request.args.get('topic', '').strip()
    difficulty = request.args.get('difficulty', '').strip()
    status = request.args.get('status', '').strip()
    keyword = request.args.get('q', '').strip()
    
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Fetch distinct topics
        cursor.execute("SELECT DISTINCT topic FROM dsa_problems ORDER BY topic")
        topics = [row[0] for row in cursor.fetchall()]
        
        # Build query
        query = '''
            SELECT p.*, 
                   COALESCE(prog.is_solved, 0) as is_solved,
                   COALESCE(prog.is_starred, 0) as is_starred,
                   prog.notes
            FROM dsa_problems p
            LEFT JOIN dsa_progress prog ON p.id = prog.problem_id AND prog.user_session = ?
            WHERE 1=1
        '''
        params = [user_sess]
        
        if topic:
            query += " AND p.topic = ?"
            params.append(topic)
            
        if difficulty:
            query += " AND p.difficulty = ?"
            params.append(difficulty)
            
        if keyword:
            query += " AND (p.title LIKE ? OR p.company_tags LIKE ? OR p.topic LIKE ?)"
            term = f"%{keyword}%"
            params.extend([term, term, term])
            
        if status == 'solved':
            query += " AND COALESCE(prog.is_solved, 0) = 1"
        elif status == 'unsolved':
            query += " AND COALESCE(prog.is_solved, 0) = 0"
        elif status == 'starred':
            query += " AND COALESCE(prog.is_starred, 0) = 1"
            
        query += " ORDER BY p.order_index ASC, p.id ASC"
        
        cursor.execute(query, params)
        problems = cursor.fetchall()
        
        # Calculate overall stats
        cursor.execute("SELECT COUNT(*) FROM dsa_problems")
        total_problems = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM dsa_progress WHERE user_session = ? AND is_solved = 1", (user_sess,))
        solved_problems = cursor.fetchone()[0]
        
        # Topic breakdown stats
        topic_stats = {}
        cursor.execute('''
            SELECT p.topic, 
                   COUNT(p.id) as total_in_topic,
                   SUM(CASE WHEN prog.is_solved = 1 THEN 1 ELSE 0 END) as solved_in_topic
            FROM dsa_problems p
            LEFT JOIN dsa_progress prog ON p.id = prog.problem_id AND prog.user_session = ?
            GROUP BY p.topic
        ''', (user_sess,))
        for row in cursor.fetchall():
            topic_stats[row[0]] = {
                'total': row[1],
                'solved': row[2] or 0,
                'pct': int(((row[2] or 0) / row[1]) * 100) if row[1] > 0 else 0
            }

    overall_pct = int((solved_problems / total_problems * 100)) if total_problems > 0 else 0

    return render_template(
        'dsa/sheet.html',
        problems=problems,
        topics=topics,
        topic_stats=topic_stats,
        total_problems=total_problems,
        solved_problems=solved_problems,
        overall_pct=overall_pct,
        selected_topic=topic,
        selected_difficulty=difficulty,
        selected_status=status,
        keyword=keyword
    )

@app.route('/api/dsa/toggle-solved', methods=['POST'])
def api_dsa_toggle_solved():
    data = request.get_json() or {}
    problem_id = data.get('problem_id')
    user_sess = get_user_session()
    
    if not problem_id:
        return jsonify({'success': False, 'message': 'Missing problem_id'}), 400
        
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT is_solved FROM dsa_progress WHERE problem_id = ? AND user_session = ?", (problem_id, user_sess))
        row = cursor.fetchone()
        
        if row is None:
            cursor.execute("INSERT INTO dsa_progress (problem_id, user_session, is_solved, solved_at) VALUES (?, ?, 1, CURRENT_TIMESTAMP)", (problem_id, user_sess))
            new_state = True
        else:
            new_state = not bool(row[0])
            cursor.execute("UPDATE dsa_progress SET is_solved = ?, solved_at = CURRENT_TIMESTAMP WHERE problem_id = ? AND user_session = ?", (1 if new_state else 0, problem_id, user_sess))
            
        # Get updated global count for user
        cursor.execute("SELECT COUNT(*) FROM dsa_progress WHERE user_session = ? AND is_solved = 1", (user_sess,))
        solved_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM dsa_problems")
        total_count = cursor.fetchone()[0]
        
    return jsonify({
        'success': True,
        'is_solved': new_state,
        'solved_count': solved_count,
        'total_count': total_count,
        'percentage': int((solved_count / total_count) * 100) if total_count else 0
    })

@app.route('/api/dsa/toggle-starred', methods=['POST'])
def api_dsa_toggle_starred():
    data = request.get_json() or {}
    problem_id = data.get('problem_id')
    user_sess = get_user_session()
    
    if not problem_id:
        return jsonify({'success': False, 'message': 'Missing problem_id'}), 400
        
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT is_starred FROM dsa_progress WHERE problem_id = ? AND user_session = ?", (problem_id, user_sess))
        row = cursor.fetchone()
        
        if row is None:
            cursor.execute("INSERT INTO dsa_progress (problem_id, user_session, is_starred) VALUES (?, ?, 1)", (problem_id, user_sess))
            new_state = True
        else:
            new_state = not bool(row[0])
            cursor.execute("UPDATE dsa_progress SET is_starred = ? WHERE problem_id = ? AND user_session = ?", (1 if new_state else 0, problem_id, user_sess))
            
    return jsonify({'success': True, 'is_starred': new_state})

@app.route('/api/dsa/problem/<int:problem_id>')
def api_get_dsa_problem(problem_id):
    user_sess = get_user_session()
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.*, COALESCE(prog.is_solved, 0) as is_solved, COALESCE(prog.is_starred, 0) as is_starred, prog.notes
            FROM dsa_problems p
            LEFT JOIN dsa_progress prog ON p.id = prog.problem_id AND prog.user_session = ?
            WHERE p.id = ?
        ''', (user_sess, problem_id))
        row = cursor.fetchone()
        
    if not row:
        return jsonify({'success': False, 'message': 'Problem not found'}), 404
        
    return jsonify({'success': True, 'problem': dict(row)})

@app.route('/api/dsa/save-notes', methods=['POST'])
def api_dsa_save_notes():
    data = request.get_json() or {}
    problem_id = data.get('problem_id')
    notes = data.get('notes', '')
    user_sess = get_user_session()
    
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM dsa_progress WHERE problem_id = ? AND user_session = ?", (problem_id, user_sess))
        row = cursor.fetchone()
        if row:
            cursor.execute("UPDATE dsa_progress SET notes = ? WHERE id = ?", (notes, row[0]))
        else:
            cursor.execute("INSERT INTO dsa_progress (problem_id, user_session, notes) VALUES (?, ?, ?)", (problem_id, user_sess, notes))
            
    return jsonify({'success': True, 'message': 'Personal notes saved!'})

# ----------------- USER DASHBOARD ROUTE -----------------
@app.route('/dashboard')
def dashboard():
    user_sess = get_user_session()
    with get_db() as conn:
        cursor = conn.cursor()
        
        # User Applications
        cursor.execute('''
            SELECT a.*, j.title, j.company, j.location, j.salary_range, j.company_logo
            FROM applications a
            JOIN jobs j ON a.job_id = j.id
            ORDER BY a.applied_at DESC
        ''')
        my_applications = cursor.fetchall()
        
        # Saved Jobs
        cursor.execute('''
            SELECT j.*, s.saved_at
            FROM saved_jobs s
            JOIN jobs j ON s.job_id = j.id
            WHERE s.user_session = ?
            ORDER BY s.saved_at DESC
        ''', (user_sess,))
        saved_jobs = cursor.fetchall()
        
        # DSA Progress
        cursor.execute("SELECT COUNT(*) FROM dsa_problems")
        total_dsa = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM dsa_progress WHERE user_session = ? AND is_solved = 1", (user_sess,))
        solved_dsa = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM dsa_progress WHERE user_session = ? AND is_starred = 1", (user_sess,))
        starred_dsa = cursor.fetchone()[0]
        
        # Starred problems
        cursor.execute('''
            SELECT p.*
            FROM dsa_progress prog
            JOIN dsa_problems p ON prog.problem_id = p.id
            WHERE prog.user_session = ? AND prog.is_starred = 1
        ''', (user_sess,))
        starred_problems = cursor.fetchall()

    return render_template(
        'dashboard.html',
        my_applications=my_applications,
        saved_jobs=saved_jobs,
        total_dsa=total_dsa,
        solved_dsa=solved_dsa,
        starred_dsa=starred_dsa,
        starred_problems=starred_problems
    )

# ----------------- PROJECT FILES & EXPLORER ROUTES -----------------
@app.route('/files')
def project_files():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_tree = []
    
    for root, dirs, files in os.walk(base_dir):
        # Exclude pycache and hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for file in sorted(files):
            if file.startswith('.') or file.endswith('.pyc') or file.endswith('.db-journal'):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir)
            size_bytes = os.path.getsize(full_path)
            
            if size_bytes < 1024:
                size_str = f"{size_bytes} B"
            elif size_bytes < 1024 * 1024:
                size_str = f"{size_bytes / 1024:.1f} KB"
            else:
                size_str = f"{size_bytes / (1024 * 1024):.1f} MB"
                
            folder = os.path.dirname(rel_path) or "root"
            file_tree.append({
                'name': file,
                'rel_path': rel_path.replace('\\', '/'),
                'folder': folder.replace('\\', '/'),
                'size': size_str,
                'size_bytes': size_bytes
            })
            
    # Group by folder
    folders = {}
    for item in file_tree:
        f = item['folder']
        if f not in folders:
            folders[f] = []
        folders[f].append(item)
        
    return render_template('files.html', folders=folders, total_files=len(file_tree), project_path=base_dir)

@app.route('/api/file-content')
def api_file_content():
    rel_path = request.args.get('path', '').strip()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.abspath(os.path.join(base_dir, rel_path))
    
    # Security check: ensure path is within base_dir
    if not full_path.startswith(base_dir) or not os.path.exists(full_path) or os.path.isdir(full_path):
        return jsonify({'error': 'Invalid file path'}), 400
        
    try:
        with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        return jsonify({
            'success': True,
            'path': rel_path,
            'content': content,
            'lines': len(content.splitlines()),
            'size': os.path.getsize(full_path)
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/download-project-zip')
def download_project_zip():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(base_dir):
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            for file in files:
                if file.startswith('.') or file.endswith('.pyc') or file == 'PriyHire_Full_Project.zip':
                    continue
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir)
                zf.write(full_path, rel_path)
    memory_file.seek(0)
    return send_file(memory_file, download_name='PriyHire_Full_Project.zip', as_attachment=True)

if __name__ == '__main__':
    # Start web server
    print("Starting PriyHire Portal on http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
