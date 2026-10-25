import sqlite3
import os
from contextlib import contextmanager

DB_PATH = os.path.join(os.path.dirname(__file__), 'careerforge.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

@contextmanager
def get_db():
    conn = get_db_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    """Initializes the database schema if tables do not exist."""
    with get_db() as conn:
        cursor = conn.cursor()
        
        # 1. Jobs Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                company_logo TEXT,
                location TEXT NOT NULL,
                job_type TEXT NOT NULL, -- Full-time, Internship, Part-time, Contract, Remote
                experience_level TEXT NOT NULL, -- Fresher, 0-1 years, 1-3 years, 3+ years
                salary_range TEXT NOT NULL,
                category TEXT NOT NULL, -- Software Engineering, Frontend, Backend, Full Stack, Data, DevOps
                description TEXT NOT NULL,
                requirements TEXT NOT NULL,
                skills TEXT NOT NULL,
                openings INTEGER DEFAULT 1,
                deadline TEXT,
                apply_url TEXT,
                company_website TEXT,
                is_featured INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # 2. Job Applications Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER NOT NULL,
                applicant_name TEXT NOT NULL,
                applicant_email TEXT NOT NULL,
                applicant_phone TEXT NOT NULL,
                resume_link TEXT,
                portfolio_link TEXT,
                experience_years TEXT,
                cover_note TEXT,
                status TEXT DEFAULT 'Under Review', -- Applied, Under Review, Shortlisted, Interview Scheduled, Rejected, Offered
                applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (job_id) REFERENCES jobs (id) ON DELETE CASCADE
            )
        ''')

        # 3. Saved Jobs Table (for user bookmarking)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS saved_jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                job_id INTEGER NOT NULL,
                user_session TEXT DEFAULT 'guest',
                saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(job_id, user_session),
                FOREIGN KEY (job_id) REFERENCES jobs (id) ON DELETE CASCADE
            )
        ''')
        
        # 4. Companies Hiring Process Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                slug TEXT NOT NULL UNIQUE,
                logo TEXT,
                industry TEXT NOT NULL,
                tier TEXT NOT NULL, -- FAANG / Tier 1 Product, Tier 2 / High Growth Unicorn, Mass IT Recruiter
                headquarters TEXT,
                overview TEXT NOT NULL,
                eligibility_criteria TEXT NOT NULL, -- JSON or structured text
                exam_pattern TEXT NOT NULL,        -- JSON or structured text
                syllabus TEXT NOT NULL,            -- JSON or structured text
                selection_process TEXT NOT NULL,   -- Step-by-step rounds
                avg_package TEXT NOT NULL,
                difficulty_level TEXT NOT NULL,    -- Moderate, Hard, Very Hard
                interview_tips TEXT NOT NULL,
                sample_questions TEXT NOT NULL,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 5. Preparation Study Notes & Modules (Aptitude, Technical, HR, DSA)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prep_modules (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL, -- aptitude, technical, hr, dsa
                subcategory TEXT NOT NULL, -- e.g., 'Quantitative', 'Operating Systems', 'Behavioral'
                title TEXT NOT NULL,
                slug TEXT NOT NULL UNIQUE,
                summary TEXT NOT NULL,
                content_html TEXT NOT NULL,
                key_formulas_or_points TEXT,
                common_mistakes TEXT,
                read_time_mins INTEGER DEFAULT 5,
                order_index INTEGER DEFAULT 0
            )
        ''')

        # 6. Practice Quizzes / Problems (Aptitude, Technical, HR, DSA)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS quiz_questions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL, -- aptitude, technical
                subtopic TEXT NOT NULL, -- 'Time and Work', 'DBMS Normalization', etc.
                question_text TEXT NOT NULL,
                option_a TEXT NOT NULL,
                option_b TEXT NOT NULL,
                option_c TEXT NOT NULL,
                option_d TEXT NOT NULL,
                correct_option TEXT NOT NULL, -- 'A', 'B', 'C', 'D'
                explanation TEXT NOT NULL,
                difficulty TEXT DEFAULT 'Medium' -- Easy, Medium, Hard
            )
        ''')

        # 7. Dedicated DSA Sheet Problems
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dsa_problems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL, -- Arrays, Strings, Linked List, Binary Search, Trees, Graphs, DP, etc.
                subtopic TEXT,
                title TEXT NOT NULL,
                slug TEXT NOT NULL,
                difficulty TEXT NOT NULL, -- Easy, Medium, Hard
                leetcode_url TEXT,
                gfg_url TEXT,
                company_tags TEXT, -- e.g. "Google, Amazon, Microsoft"
                problem_statement TEXT NOT NULL,
                constraints TEXT,
                hints TEXT,
                solution_approach TEXT,
                time_complexity TEXT,
                space_complexity TEXT,
                solution_python TEXT,
                solution_cpp TEXT,
                solution_java TEXT,
                order_index INTEGER DEFAULT 0
            )
        ''')

        # 8. DSA User Progress (Synced with local/session state)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS dsa_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                problem_id INTEGER NOT NULL,
                user_session TEXT DEFAULT 'guest',
                is_solved INTEGER DEFAULT 0,
                is_starred INTEGER DEFAULT 0,
                notes TEXT,
                solved_at TIMESTAMP,
                UNIQUE(problem_id, user_session),
                FOREIGN KEY (problem_id) REFERENCES dsa_problems (id) ON DELETE CASCADE
            )
        ''')

if __name__ == '__main__':
    init_db()
    print("Database schema successfully created!")
