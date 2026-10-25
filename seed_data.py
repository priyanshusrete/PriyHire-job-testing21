import json
import sqlite3
from database import get_db, init_db

def seed_all():
    init_db()
    
    with get_db() as conn:
        cursor = conn.cursor()
        
        # Check if already seeded
        cursor.execute("SELECT COUNT(*) FROM jobs")
        if cursor.fetchone()[0] > 0:
            print("Database already contains data. Skipping re-seed.")
            return

        print("Seeding Jobs...")
        jobs_data = [
            (
                "Software Development Engineer I (SDE-1)",
                "Amazon",
                "https://images.unsplash.com/photo-1523474255658-4af61b1614ff?auto=format&fit=crop&w=120&h=120&q=80",
                "Bangalore, India (Hybrid)",
                "Full-time",
                "0-2 years",
                "₹18,00,000 - ₹24,00,000 / yr",
                "Software Engineering",
                "Amazon is seeking passionate and customer-obsessed SDE-1s to join our AWS Cloud Infrastructure team. You will design, build, and deploy high-scale distributed microservices.",
                "• Strong proficiency in Java, C++, or Python\n• Sound understanding of Data Structures, Algorithms, and Object-Oriented Design\n• Experience with REST APIs and distributed systems fundamentals\n• B.Tech/B.E. in CS/IT/ECE or related discipline with 7.0+ CGPA",
                "Java, Python, Distributed Systems, Data Structures, Algorithms, AWS, Git",
                8,
                "2026-11-30",
                "https://amazon.jobs",
                "https://amazon.com",
                1
            ),
            (
                "Associate Software Engineer",
                "Google",
                "https://images.unsplash.com/photo-1572021335469-31706a17aaef?auto=format&fit=crop&w=120&h=120&q=80",
                "Hyderabad, India (Hybrid)",
                "Full-time",
                "Fresher - 1 year",
                "₹22,00,000 - ₹30,00,000 / yr",
                "Software Engineering",
                "Join Google's Core Engineering team to solve tough algorithmic challenges that affect billions of global users. You will write clean, well-tested code and collaborate with world-class engineers.",
                "• Deep foundation in Algorithms, Complexity Analysis, and Data Structures\n• Experience in one or more programming languages (C++, Go, Java, Python)\n• Solid understanding of operating systems and networking concepts\n• B.Tech/M.Tech in Computer Science or equivalent",
                "C++, Python, Algorithms, Linux, Distributed Computing, Problem Solving",
                5,
                "2026-12-15",
                "https://careers.google.com",
                "https://google.com",
                1
            ),
            (
                "Graduate Trainee Engineer (Digital / Prime)",
                "Tata Consultancy Services (TCS)",
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=120&h=120&q=80",
                "Pan India (Mumbai / Pune / Chennai / Kolkata / Delhi NCR)",
                "Full-time",
                "Fresher",
                "₹7,00,000 - ₹9,50,000 / yr",
                "Software Engineering",
                "TCS Digital and Prime cadence hiring for young engineering minds. High-impact roles in AI, Cloud, Cyber Security, IoT, and Full Stack product engineering.",
                "• B.Tech/B.E./M.Tech/MCA batches with minimum 60% or 6.0 CGPA throughout 10th, 12th, and Degree\n• No active backlogs allowed at time of joining\n• Excellent problem solving and quantitative aptitude skills",
                "Python, Java, SQL, Cloud Basics, Problem Solving, Data Analysis",
                150,
                "2026-11-20",
                "https://www.tcs.com/careers",
                "https://tcs.com",
                1
            ),
            (
                "Specialist Programmer (Power Programmer)",
                "Infosys",
                "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=120&h=120&q=80",
                "Bangalore / Pune / Hyderabad",
                "Full-time",
                "Fresher",
                "₹9,50,000 - ₹12,00,000 / yr",
                "Software Engineering",
                "Specialist Programmer is Infosys's elite technical tier role. Selected through HackWithInfy or National Level Coding tests. You will work on cutting-edge enterprise architecture.",
                "• High-level competitive programming skills (DP, Graphs, Advanced Trees)\n• Proficiency in Python, Java, or C++\n• Good understanding of modern software architecture\n• All branches eligible with 65% aggregate",
                "Competitive Programming, Java, Spring Boot, Microservices, React, Docker",
                40,
                "2026-11-25",
                "https://www.infosys.com/careers",
                "https://infosys.com",
                1
            ),
            (
                "Frontend Engineer - React / Next.js",
                "Razorpay",
                "https://images.unsplash.com/photo-1551434678-e076c223a692?auto=format&fit=crop&w=120&h=120&q=80",
                "Bangalore, India (Remote Available)",
                "Full-time",
                "1-3 years",
                "₹14,00,000 - ₹20,00,000 / yr",
                "Frontend",
                "Build pixel-perfect, accessible, and ultra-fast fintech checkout experiences used by millions of merchants every single day.",
                "• Strong grasp of modern JavaScript (ES6+), TypeScript, and React\n• Understanding of state management (Zustand/Redux), web vitals, and rendering performance\n• Passion for sleek UI/UX and responsive layouts",
                "React, TypeScript, Next.js, Tailwind CSS, REST APIs, Webpack",
                6,
                "2026-12-05",
                "https://razorpay.com/jobs",
                "https://razorpay.com",
                0
            ),
            (
                "Backend Engineer (Go / Node.js)",
                "Swiggy",
                "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=120&h=120&q=80",
                "Bangalore, India",
                "Full-time",
                "1-3 years",
                "₹16,00,000 - ₹22,00,000 / yr",
                "Backend",
                "Work on Swiggy's high-throughput order dispatch, routing, and lightning-fast logistics engine serving 100,000+ requests per second.",
                "• Hands-on experience with Go or Node.js/TypeScript in production\n• Familiarity with Kafka/RabbitMQ message queues and Redis caching\n• Solid understanding of relational and NoSQL databases",
                "Golang, Node.js, Kafka, Redis, PostgreSQL, Docker, Microservices",
                4,
                "2026-11-28",
                "https://careers.swiggy.com",
                "https://swiggy.com",
                0
            ),
            (
                "Data Analyst Trainee",
                "Accenture",
                "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=120&h=120&q=80",
                "Gurugram / Noida / Bangalore",
                "Full-time",
                "Fresher",
                "₹5,50,000 - ₹7,00,000 / yr",
                "Data",
                "Analyze large-scale enterprise data to derive actionable business intelligence, build KPI dashboards, and streamline data pipelines.",
                "• Strong SQL querying skills (Joins, CTEs, Window Functions)\n• Working knowledge of Python (Pandas, NumPy) and PowerBI / Tableau\n• Good analytical and business communication skills",
                "SQL, Python, PowerBI, Excel, Data Visualization, Statistics",
                30,
                "2026-12-10",
                "https://accenture.com/careers",
                "https://accenture.com",
                0
            ),
            (
                "Junior Cloud & DevOps Engineer",
                "Capgemini",
                "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=120&h=120&q=80",
                "Hyderabad / Pune",
                "Full-time",
                "0-2 years",
                "₹6,00,000 - ₹8,50,000 / yr",
                "DevOps",
                "Join Capgemini Cloud Services to manage CI/CD pipelines, containerized deployments, and infrastructure monitoring across AWS and Azure environments.",
                "• Basic knowledge of Linux operating system and shell scripting\n• Hands-on experience or coursework with Docker, Kubernetes, and Git\n• Understanding of AWS or Azure cloud primitives",
                "Linux, Docker, Kubernetes, AWS, CI/CD, GitHub Actions, Bash",
                15,
                "2026-12-01",
                "https://capgemini.com/careers",
                "https://capgemini.com",
                0
            ),
            (
                "AI/ML Research Intern",
                "Microsoft",
                "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=120&h=120&q=80",
                "Bangalore / Hyderabad, India",
                "Internship",
                "Fresher / Student",
                "₹80,000 - ₹1,25,000 / month",
                "Software Engineering",
                "Collaborate with Microsoft Research (MSR) India on foundational LLM alignment, agentic workflows, and high-performance neural systems.",
                "• Currently enrolled in B.Tech, M.Tech, or MS in Computer Science\n• Strong Python skills and familiarity with PyTorch, Transformers, or Hugging Face\n• Solid foundation in Linear Algebra, Probability, and Optimization",
                "Python, PyTorch, Deep Learning, NLP, LLMs, Git",
                10,
                "2026-11-18",
                "https://careers.microsoft.com",
                "https://microsoft.com",
                1
            ),
            (
                "Full Stack Web Developer Intern",
                "Zomato",
                "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=120&h=120&q=80",
                "Gurgaon, India (On-site)",
                "Internship",
                "Fresher",
                "₹50,000 - ₹75,000 / month",
                "Full Stack",
                "Build dynamic features for millions of foodies and delivery partners across India. Work across React, Node.js, and Redis cache clusters.",
                "• Understanding of full-stack web development cycle\n• Proficiency with React.js, Node.js, Express, and MongoDB/PostgreSQL\n• Ability to write clean, maintainable modular code",
                "React, Node.js, JavaScript, Express, MongoDB, Tailwind CSS",
                5,
                "2026-11-22",
                "https://zomato.com/careers",
                "https://zomato.com",
                0
            )
        ]

        cursor.executemany('''
            INSERT INTO jobs (
                title, company, company_logo, location, job_type, experience_level,
                salary_range, category, description, requirements, skills, openings,
                deadline, apply_url, company_website, is_featured
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', jobs_data)

        print("Seeding Companies Hiring Process Data...")
        companies_data = [
            (
                "Tata Consultancy Services (TCS)",
                "tcs",
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=120&h=120&q=80",
                "IT Services & Consulting",
                "Mass IT Recruiter / Enterprise",
                "Mumbai, India",
                "Tata Consultancy Services is an Indian multinational information technology services and consulting company with over 600,000 employees globally.",
                json.dumps({
                    "criteria": [
                        "Minimum 60% or 6.0 CGPA throughout academics (Class 10th, 12th, Diploma, and Graduation)",
                        "Highest academic degree must be completed within permissible duration",
                        "Maximum 1 active backlog permitted at the time of test (must clear before joining)",
                        "Total academic gap should not exceed 24 months across all stages",
                        "Eligible Batches: B.E., B.Tech, M.E., M.Tech, MCA, M.Sc (CS/IT)"
                    ]
                }),
                json.dumps({
                    "cadences": [
                        {
                            "track": "TCS Ninja (Standard - ₹3.36 to ₹3.6 LPA)",
                            "rounds": "Cognitive Skills (Numerical Ability, Verbal Ability, Reasoning Ability) + Foundation Programming",
                            "duration": "75 minutes"
                        },
                        {
                            "track": "TCS Digital (Advanced - ₹7.0 to ₹7.5 LPA)",
                            "rounds": "Advanced Quantitative & Reasoning (25 mins) + Advanced Coding (2 problems - 60 mins)",
                            "duration": "85 minutes"
                        },
                        {
                            "track": "TCS Prime (Premium - ₹9.0 to ₹11.5 LPA)",
                            "rounds": "Shortlisted via top percentile in NQT Advanced Coding + Hackathons",
                            "duration": "Comprehensive Technical Assessment"
                        }
                    ],
                    "marking_scheme": "No negative marking in Foundation; sectional time limits are strictly enforced."
                }),
                json.dumps({
                    "sections": [
                        {
                            "name": "Numerical Ability",
                            "topics": "Number Systems, Time & Work, Speed & Distance, Percentages, Profit & Loss, Ratio & Proportion, Permutations"
                        },
                        {
                            "name": "Reasoning Ability",
                            "topics": "Data Arrangements, Syllogisms, Blood Relations, Coding-Decoding, Venn Diagrams, Visual Reasoning"
                        },
                        {
                            "name": "Verbal Ability",
                            "topics": "Reading Comprehension, Sentence Completion, Spotting Errors, Para Jumbles, Vocabulary"
                        },
                        {
                            "name": "Hands-on Coding",
                            "topics": "Arrays, Strings, Matrix Manipulation, Hashing, Sorting, Basic Math Algorithms (GCD, Primes, Base Conversion)"
                        }
                    ]
                }),
                json.dumps([
                    {"round": "Round 1", "name": "TCS NQT Online Assessment", "details": "Conducted on TCS iON platform. Foundation + Advanced sections with camera proctoring."},
                    {"round": "Round 2", "name": "Technical Interview (TR)", "details": "Focus on core subjects (DBMS, OOP, OS), chosen programming language, and final year project."},
                    {"round": "Round 3", "name": "Managerial Interview (MR)", "details": "Situational questions, team conflicts, client scenarios, project challenges."},
                    {"round": "Round 4", "name": "HR Interview", "details": "Document verification, willingness to relocate, shift flexibility, background check."}
                ]),
                "₹3.6 LPA (Ninja) | ₹7.2 LPA (Digital) | ₹9.5 LPA (Prime)",
                "Moderate",
                "• Master basic array and string manipulation in C/C++/Java/Python.\n• Sectional timers mean you cannot revisit previous sections; practice time allocation.\n• Be thoroughly prepared with your final-year college project architecture and schema.",
                "1. Given an array of integers, find the pair with the maximum product.\n2. Explain ACID properties with real-world banking examples.\n3. What is the difference between Process and Thread?\n4. Write a program to reverse words in a given sentence without using split functions."
            ),
            (
                "Infosys",
                "infosys",
                "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=120&h=120&q=80",
                "IT Services & Consulting",
                "Mass IT Recruiter / Product Engineering",
                "Bangalore, India",
                "Infosys is a global leader in next-generation digital services and consulting, enabling clients in more than 50 countries to navigate their digital transformation.",
                json.dumps({
                    "criteria": [
                        "Minimum 65% or 6.5 CGPA in 10th, 12th, and B.Tech / M.Tech / MCA",
                        "No standing active arrears / backlogs permitted at the interview stage",
                        "Eligible branches: All branches eligible (including Mechanical, Civil, Electrical for SE track)",
                        "Maximum 2 years of education gap allowed"
                    ]
                }),
                json.dumps({
                    "cadences": [
                        {
                            "track": "Systems Engineer (SE - ₹3.6 LPA)",
                            "rounds": "Reasoning Ability (15 Qs - 25m), Technical Ability/Math (10 Qs - 35m), Verbal (20 Qs - 20m), Pseudocode (5 Qs - 10m), Numerical Puzzle (4 Qs - 10m)",
                            "duration": "100 minutes"
                        },
                        {
                            "track": "Digital Specialist Engineer (DSE - ₹6.25 LPA)",
                            "rounds": "3 Coding questions (Easy, Medium, Medium-Hard) - 180 minutes",
                            "duration": "180 minutes"
                        },
                        {
                            "track": "Specialist Programmer (SP - ₹9.5 LPA)",
                            "rounds": "3 Advanced Coding questions (Medium, Hard, DP/Graph) - 180 minutes",
                            "duration": "180 minutes"
                        }
                    ],
                    "marking_scheme": "No negative marking. Each question has a fixed individual timer in the SE exam!"
                }),
                json.dumps({
                    "sections": [
                        {
                            "name": "Mathematical & Critical Reasoning",
                            "topics": "Data Sufficiency, Syllogisms, Seating Arrangements, Coding Pattern, Number Series"
                        },
                        {
                            "name": "Pseudocode Round",
                            "topics": "Recursion tracing, Bitwise operators, Loop execution, Pointer logic in C"
                        },
                        {
                            "name": "Coding (DSE/SP)",
                            "topics": "Greedy algorithms, Dynamic Programming, Segment Trees, Graph BFS/DFS, Disjoint Set Union"
                        }
                    ]
                }),
                json.dumps([
                    {"round": "Round 1", "name": "Online Test / HackWithInfy", "details": "National qualification test on Infosys testing portal."},
                    {"round": "Round 2", "name": "Technical + HR Combined Interview", "details": "Live code walkthrough of HackWithInfy solutions, OOP, SQL queries, problem solving."}
                ]),
                "₹3.6 LPA (SE) | ₹6.5 LPA (DSE) | ₹9.5 - ₹12 LPA (SP)",
                "Moderate to Hard (SP is Hard)",
                "• In the Systems Engineer test, time management is paramount because questions are timed individually.\n• For SP and DSE, solve 2 full problems with optimal time complexity to guarantee an interview call.",
                "1. Find the length of the longest palindromic substring.\n2. Explain 2NF, 3NF, and BCNF with student database examples.\n3. Implement a Stack using two Queues.\n4. Write a SQL query to fetch the 3rd highest salary using DENSE_RANK()."
            ),
            (
                "Amazon",
                "amazon",
                "https://images.unsplash.com/photo-1523474255658-4af61b1614ff?auto=format&fit=crop&w=120&h=120&q=80",
                "E-Commerce & Cloud Computing",
                "FAANG / Tier 1 Product",
                "Seattle, USA (HQ) / Bangalore, India",
                "Amazon is guided by four principles: customer obsession, passion for invention, commitment to operational excellence, and long-term thinking.",
                json.dumps({
                    "criteria": [
                        "B.Tech / B.E. / M.Tech in CS/IT/ECE or related STEM degrees",
                        "Minimum 7.0 CGPA or 70% equivalent with no current backlogs",
                        "High fluency in at least one modern language (Java, C++, or Python)"
                    ]
                }),
                json.dumps({
                    "cadences": [
                        {
                            "track": "Online Assessment (OA1 + OA2)",
                            "rounds": "Coding Assessment (2 DSA problems - 70 mins) + Work Style Assessment / SDE Simulation (16 Leadership Principles - 40 mins)",
                            "duration": "110 minutes"
                        }
                    ],
                    "marking_scheme": "All test cases (public + hidden performance test cases) must pass."
                }),
                json.dumps({
                    "sections": [
                        {
                            "name": "Coding Round",
                            "topics": "Arrays, Hash Maps, Priority Queues, Binary Trees, Graph Traversal, Dynamic Programming, Sliding Window"
                        },
                        {
                            "name": "Work Style Assessment",
                            "topics": "Amazon 16 Leadership Principles (Customer Obsession, Ownership, Bias for Action, Dive Deep)"
                        }
                    ]
                }),
                json.dumps([
                    {"round": "Round 1", "name": "Online Assessment (OA)", "details": "2 DSA problems on HackerRank + 15 min explanation write-up + Work Styles survey."},
                    {"round": "Round 2", "name": "Technical Interview 1", "details": "1 LP question (STAR method) + 1-2 medium DSA problems on live collaborative editor."},
                    {"round": "Round 3", "name": "Technical Interview 2", "details": "1 LP question + Advanced Trees/Graphs/DP problem + Space/Time complexity deep dive."},
                    {"round": "Round 4", "name": "Bar Raiser / HM Round", "details": "Conducted by an independent evaluator. Heavy emphasis on Amazon Leadership Principles and low-level system design."}
                ]),
                "₹18 - ₹28 LPA (Base ₹15-18L + Stocks + Joining Bonus)",
                "Hard",
                "• Every single round dedicates 15-20 minutes to Amazon's 16 Leadership Principles. Frame your stories in STAR format.\n• Always communicate your thought process out loud before writing a single line of code.",
                "1. Course Schedule II (Topological Sort).\n2. LRU Cache Implementation with O(1) get and put.\n3. Trapping Rain Water problem.\n4. STAR question: 'Tell me about a time when you disagreed with a colleague or mentor and how you resolved it.'"
            ),
            (
                "Google",
                "google",
                "https://images.unsplash.com/photo-1572021335469-31706a17aaef?auto=format&fit=crop&w=120&h=120&q=80",
                "Internet & Technology",
                "FAANG / Tier 1 Product",
                "Mountain View, USA / Hyderabad, India",
                "Google's mission is to organize the world's information and make it universally accessible and useful.",
                json.dumps({
                    "criteria": [
                        "B.Tech / M.Tech / PhD in Computer Science, Software Engineering, or related fields",
                        "Exceptional problem-solving, algorithms, and data structure fluency",
                        "No strict CGPA threshold, but 7.5+ is standard for on-campus & referrals"
                    ]
                }),
                json.dumps({
                    "cadences": [
                        {
                            "track": "Google Online Challenge (GOC)",
                            "rounds": "2 Algorithmic Coding Problems (Medium to Hard level)",
                            "duration": "60 minutes"
                        }
                    ],
                    "marking_scheme": "Automated evaluation testing correctness, asymptotic optimality, and extreme edge cases."
                }),
                json.dumps({
                    "sections": [
                        {
                            "name": "Algorithmic Challenges",
                            "topics": "Dynamic Programming, Trees, Segment Trees, Union Find, Graph Theory, Combinatorics, Dijkstra, Binary Search"
                        },
                        {
                            "name": "Googleyness & Leadership",
                            "topics": "Navigating ambiguity, intellectual humility, doing the right thing, collaboration"
                        }
                    ]
                }),
                json.dumps([
                    {"round": "Round 1", "name": "Google Online Challenge (GOC)", "details": "HackerEarth / internal test with 2 high-level algorithmic problems."},
                    {"round": "Round 2", "name": "Technical Screen", "details": "45-minute live coding session on Google Docs or CoderPad."},
                    {"round": "Round 3-5", "name": "Onsite / Virtual Loop (3 Tech + 1 Googleyness)", "details": "Rigorous algorithm problem solving, edge-case testing, and behavioral fit."}
                ]),
                "₹25 - ₹40+ LPA (Base + GSU Stocks + Bonus)",
                "Very Hard",
                "• Avoid guessing! Clarify problem constraints and write production-grade, modular, variable-named code on a plain Google Doc without autocomplete.\n• Dry-run your solution with sample and corner cases before saying you are finished.",
                "1. Median of Two Sorted Arrays (O(log(m+n))).\n2. Word Ladder II (BFS + DFS Backtracking).\n3. Alien Dictionary (Graph cycle detection and Topological Sort).\n4. Design an efficient hit counter for 100M queries per second."
            ),
            (
                "Wipro",
                "wipro",
                "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=120&h=120&q=80",
                "IT Services & Consulting",
                "Mass IT Recruiter",
                "Bangalore, India",
                "Wipro Limited is a leading technology services and consulting company focused on building innovative solutions that address clients' most complex digital transformation needs.",
                json.dumps({
                    "criteria": [
                        "60% or 6.0 CGPA in 10th, 12th, and Graduation",
                        "Up to 1 backlog permitted at the time of assessment",
                        "Maximum 3 years of academic education gap allowed"
                    ]
                }),
                json.dumps({
                    "cadences": [
                        {
                            "track": "Elite National Talent Hunt (ENTH - ₹3.5 LPA)",
                            "rounds": "Aptitude (Quants, Logical, Verbal - 48 mins) + Essay Writing (20 mins) + Coding (2 Qs - 60 mins)",
                            "duration": "128 minutes"
                        },
                        {
                            "track": "Turbo Upgrade (₹6.5 LPA)",
                            "rounds": "Shortlisted via high test score followed by Advanced Coding Challenge",
                            "duration": "60 minutes"
                        }
                    ],
                    "marking_scheme": "No negative marking. Essay writing is automatically checked for grammar and clarity."
                }),
                json.dumps({
                    "sections": [
                        {
                            "name": "Quantitative & Logical",
                            "topics": "Number properties, Profit & loss, Coding-Decoding, Statements & Conclusions, Direction sense"
                        },
                        {
                            "name": "Written Communication",
                            "topics": "200-400 words professional essay on socio-technological trends"
                        },
                        {
                            "name": "Coding",
                            "topics": "Pattern printing, Arrays, String manipulations, basic search and sorting"
                        }
                    ]
                }),
                json.dumps([
                    {"round": "Round 1", "name": "Wipro Elite Online Assessment", "details": "Conducted on AMCAT / Mettl platform with automated webcam proctoring."},
                    {"round": "Round 2", "name": "Technical Interview", "details": "Basic programming fundamentals, OOP concepts, final-year project."},
                    {"round": "Round 3", "name": "HR Interview", "details": "Relocation agreement, service bonds, communication checks."}
                ]),
                "₹3.5 LPA (Elite) | ₹6.5 LPA (Turbo)",
                "Easy to Moderate",
                "• Do not copy-paste during the essay round as the automated parser flags plagiarism immediately.\n• Ensure your microphone and lighting are clear for the proctoring software.",
                "1. Check if two strings are anagrams of each other.\n2. Print the Fibonacci series up to N using recursion and iteration.\n3. Difference between Primary Key and Unique Key in SQL."
            ),
            (
                "Microsoft",
                "microsoft",
                "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=120&h=120&q=80",
                "Software & Cloud Services",
                "FAANG / Tier 1 Product",
                "Redmond, USA / Hyderabad, India",
                "Microsoft enables digital transformation for the era of an intelligent cloud and an intelligent edge. Home to Windows, Azure, Office, and Xbox.",
                json.dumps({
                    "criteria": [
                        "B.Tech / B.E / M.Tech in CS / IT or related circuital branches",
                        "Minimum 7.0 CGPA without any backlogs",
                        "Strong foundation in OOP, OS, Data Structures, and System Architecture"
                    ]
                }),
                json.dumps({
                    "cadences": [
                        {
                            "track": "Software Engineer (Full-time & Intern)",
                            "rounds": "Online Coding Assessment (3 problems - 90 mins on Codility/Mettl)",
                            "duration": "90 minutes"
                        }
                    ],
                    "marking_scheme": "Codility score depends on correctness and performance benchmarks against large inputs."
                }),
                json.dumps({
                    "sections": [
                        {
                            "name": "Codility Online Test",
                            "topics": "Bit manipulation, Greedy algorithms, Two Pointers, Trees, Dynamic Programming"
                        },
                        {
                            "name": "System Concepts",
                            "topics": "Virtual Memory, Paging, Concurrency, Mutex vs Semaphore, Indexing in Databases"
                        }
                    ]
                }),
                json.dumps([
                    {"round": "Round 1", "name": "Online Coding Assessment", "details": "3 problem statements on Codility platform."},
                    {"round": "Round 2", "name": "Technical Interview 1", "details": "DSA coding + Data structure internals (Hash tables, Red-Black Trees)."},
                    {"round": "Round 3", "name": "Technical Interview 2", "details": "Design patterns, Low-Level Design (LLD), concurrency and thread safety."},
                    {"round": "Round 4", "name": "AA (As Appropriate) / Director Round", "details": "Cultural alignment, project architecture, edge-case resilience."}
                ]),
                "₹20 - ₹28 LPA (Base + Bonus + Microsoft Stock Options)",
                "Hard",
                "• Microsoft interviewers love clean object-oriented design and thread safety considerations.\n• Practice writing code without any compiler help and proactively write unit test cases.",
                "1. Clone a Graph with deep copying of vertices and edges.\n2. Serialize and Deserialize a Binary Tree.\n3. Implement an LRU and LFU cache.\n4. Design a parking lot system using SOLID principles."
            )
        ]

        cursor.executemany('''
            INSERT INTO companies (
                name, slug, logo, industry, tier, headquarters, overview,
                eligibility_criteria, exam_pattern, syllabus, selection_process,
                avg_package, difficulty_level, interview_tips, sample_questions
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', companies_data)

        print("Seeding Preparation Notes & Modules...")
        prep_modules_data = [
            # Aptitude Modules
            (
                "aptitude",
                "Quantitative Aptitude",
                "Time and Work - Formulas & Shortcut Tricks",
                "time-and-work-formulas",
                "Master Time & Work problems with the LCM method, efficiency ratios, and man-days formulas.",
                """
                <h3>Core Concept: The LCM Method</h3>
                <p>The standard school method assigns work as <code>1</code> unit, but in competitive exams, calculate the <strong>LCM of total days</strong> taken by individual workers to get the total work units. This avoids working with fractions!</p>
                
                <div class="bg-indigo-50 border-l-4 border-indigo-600 p-4 my-4 rounded-r">
                    <h4 class="font-bold text-indigo-900">Key Golden Formulas:</h4>
                    <ul class="list-disc pl-5 mt-2 space-y-1 text-indigo-800">
                        <li><strong>Work = Efficiency × Time</strong></li>
                        <li><strong>Total Work = LCM(Days of A, Days of B, ...)</strong></li>
                        <li><strong>Efficiency of Worker = Total Work ÷ Days taken by worker</strong></li>
                        <li><strong>Man-Days Formula:</strong> <code>(M₁ × D₁ × H₁) / W₁ = (M₂ × D₂ × H₂) / W₂</code></li>
                    </ul>
                </div>

                <h4>Example Walkthrough:</h4>
                <p><em>Problem:</em> A can complete a work in 10 days, and B can complete the same work in 15 days. In how many days can they complete it working together?</p>
                <ol class="list-decimal pl-6 space-y-2 mt-2">
                    <li><strong>Step 1:</strong> Find LCM of 10 and 15 = <strong>30 units</strong> (Total Work).</li>
                    <li><strong>Step 2:</strong> A's efficiency = 30 / 10 = <strong>3 units/day</strong>.</li>
                    <li><strong>Step 3:</strong> B's efficiency = 30 / 15 = <strong>2 units/day</strong>.</li>
                    <li><strong>Step 4:</strong> Combined efficiency = 3 + 2 = <strong>5 units/day</strong>.</li>
                    <li><strong>Step 5:</strong> Time taken = Total Work / Combined Efficiency = 30 / 5 = <strong>6 days</strong>.</li>
                </ol>

                <h4 class="mt-6">Pipes and Cisterns Equivalence:</h4>
                <p>Inflow pipes perform <strong>positive work</strong> (filling). Outflow/Leak pipes perform <strong>negative work</strong> (emptying). Subtract their efficiency from the total!</p>
                """,
                "• Work = Efficiency × Time\n• (M1 × D1 × H1)/W1 = (M2 × D2 × H2)/W2\n• Always use LCM of individual days as total units",
                "Adding times directly (e.g. 10 + 15 = 25 days) instead of adding reciprocal efficiencies.",
                8,
                1
            ),
            (
                "aptitude",
                "Quantitative Aptitude",
                "Speed, Time & Distance - Relative Speed & Trains",
                "speed-time-and-distance",
                "Quickly solve problems on trains, average speed, and relative motion with proven tricks.",
                """
                <h3>Unit Conversions & Base Formulas</h3>
                <p>Always verify units before calculating. Most exam questions give speed in km/h and time in seconds!</p>
                
                <div class="bg-indigo-50 border-l-4 border-indigo-600 p-4 my-4 rounded-r">
                    <ul class="list-disc pl-5 space-y-1 text-indigo-800">
                        <li><strong>Convert km/h to m/s:</strong> Multiply by <code>5 / 18</code></li>
                        <li><strong>Convert m/s to km/h:</strong> Multiply by <code>18 / 5</code></li>
                        <li><strong>Average Speed (Equal Distances):</strong> <code>(2 × S₁ × S₂) / (S₁ + S₂)</code> (Harmonic Mean)</li>
                        <li><strong>Average Speed (General):</strong> <code>Total Distance Covered / Total Time Taken</code></li>
                    </ul>
                </div>

                <h4>Relative Speed Rules:</h4>
                <ul class="list-disc pl-5 space-y-2">
                    <li><strong>Opposite Directions:</strong> Objects moving toward each other: <code>Relative Speed = S₁ + S₂</code></li>
                    <li><strong>Same Direction:</strong> Objects moving in the same direction: <code>Relative Speed = |S₁ - S₂|</code></li>
                </ul>

                <h4 class="mt-4">Train Crossing Rules:</h4>
                <ul class="list-disc pl-5 space-y-2">
                    <li>Crossing a pole/standing man (negligible length): <code>Distance = Length of Train (L₁)</code></li>
                    <li>Crossing a platform or bridge of length L₂: <code>Distance = L₁ + L₂</code></li>
                    <li>Two trains crossing each other: <code>Total Distance = L₁ + L₂</code></li>
                </ul>
                """,
                "• km/h to m/s: multiply by 5/18\n• Opp direction speed: S1 + S2\n• Same direction speed: |S1 - S2|\n• Crossing platform: Distance = L_train + L_platform",
                "Using arithmetic mean (S1+S2)/2 for average speed when distances are equal instead of harmonic mean.",
                7,
                2
            ),
            (
                "aptitude",
                "Logical Reasoning",
                "Syllogisms & Venn Diagram Analysis",
                "syllogisms-venn-diagrams",
                "Learn the 100-50 method and Venn Diagram logic to solve syllogism conclusions with 100% accuracy.",
                """
                <h3>Standard Propositions in Syllogisms</h3>
                <p>Every syllogism statement falls into one of four standard categories:</p>
                <div class="grid grid-cols-2 gap-4 my-3 text-sm">
                    <div class="p-3 bg-gray-50 border rounded"><strong>A Type (Universal Affirmative):</strong> 'All A are B' (100% of A belongs to B)</div>
                    <div class="p-3 bg-gray-50 border rounded"><strong>E Type (Universal Negative):</strong> 'No A is B' (0% overlap between A and B)</div>
                    <div class="p-3 bg-gray-50 border rounded"><strong>I Type (Particular Affirmative):</strong> 'Some A are B' (At least one A is B)</div>
                    <div class="p-3 bg-gray-50 border rounded"><strong>O Type (Particular Negative):</strong> 'Some A are not B'</div>
                </div>

                <h4>The Golden Rules of Conclusion:</h4>
                <ol class="list-decimal pl-6 space-y-2">
                    <li><strong>Two Positive Premises</strong> always produce a <strong>Positive Conclusion</strong>.</li>
                    <li><strong>One Negative Premise</strong> always produces a <strong>Negative Conclusion</strong>.</li>
                    <li><strong>Two Negative Premises</strong> yield <strong>No Definite Conclusion</strong>.</li>
                    <li><strong>'Possibility' cases:</strong> If something is not prohibited by any premise, it can be true as a possibility!</li>
                </ol>
                """,
                "• Two positive statements -> positive conclusion\n• One negative statement -> negative conclusion\n• 'Some' implies at least one, not necessarily all",
                "Confusing 'Some A are B' with 'All A are B' or assuming symmetry for 'Some A are not B'.",
                6,
                3
            ),
            
            # Technical Core Modules
            (
                "technical",
                "Operating Systems",
                "Process vs Thread & CPU Scheduling Demystified",
                "os-process-threads-scheduling",
                "Deep dive into OS execution models, Context Switching, Preemptive vs Non-Preemptive scheduling algorithms.",
                """
                <h3>Process vs Thread Comparison</h3>
                <table class="w-full text-left text-sm border-collapse my-4">
                    <thead>
                        <tr class="bg-gray-100 border-b">
                            <th class="p-2 font-semibold">Parameter</th>
                            <th class="p-2 font-semibold">Process</th>
                            <th class="p-2 font-semibold">Thread</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b"><td class="p-2 font-medium">Memory</td><td class="p-2">Isolated address space (Code, Data, Heap, Stack)</td><td class="p-2">Shares Code, Data, and Heap with parent; own Stack & Registers</td></tr>
                        <tr class="border-b"><td class="p-2 font-medium">Overhead</td><td class="p-2">Heavyweight creation and termination</td><td class="p-2">Lightweight creation and context switch</td></tr>
                        <tr class="border-b"><td class="p-2 font-medium">Communication</td><td class="p-2">IPC (Pipes, Sockets, Shared Memory, Message Queues)</td><td class="p-2">Direct memory read/write (requires synchronization locks)</td></tr>
                        <tr><td class="p-2 font-medium">Failure Impact</td><td class="p-2">One process crash does not affect other processes</td><td class="p-2">One thread crash can terminate the entire process</td></tr>
                    </tbody>
                </table>

                <h3 class="mt-6">CPU Scheduling Algorithms</h3>
                <div class="space-y-3">
                    <div class="p-3 bg-gray-50 border rounded">
                        <strong>1. FCFS (First Come First Serve):</strong> Non-preemptive. Suffers from the <em>Convoy Effect</em> (short processes waiting behind long CPU-bound process).
                    </div>
                    <div class="p-3 bg-gray-50 border rounded">
                        <strong>2. SJF / SRTF (Shortest Job First):</strong> Optimal average waiting time! Preemptive version is called Shortest Remaining Time First (SRTF). Vulnerable to <em>starvation</em> of long jobs.
                    </div>
                    <div class="p-3 bg-gray-50 border rounded">
                        <strong>3. Round Robin (RR):</strong> Preemptive using a fixed <em>Time Quantum (q)</em>. Fair scheduling for interactive multi-user systems. If q is too small, context switch overhead dominates.
                    </div>
                </div>

                <h3 class="mt-6">The 4 Necessary Conditions for Deadlock (Coffman Conditions)</h3>
                <p>Deadlock can occur if and only if all four conditions hold simultaneously:</p>
                <ol class="list-decimal pl-6 space-y-1">
                    <li><strong>Mutual Exclusion:</strong> At least one resource is held in non-shareable mode.</li>
                    <li><strong>Hold and Wait:</strong> A process is holding at least one resource and requesting additional resources held by others.</li>
                    <li><strong>No Preemption:</strong> Resources cannot be forcibly confiscated from a process holding them.</li>
                    <li><strong>Circular Wait:</strong> A closed chain of processes exists such that each process holds a resource needed by the next.</li>
                </ol>
                """,
                "• Threads share Code, Data, Heap; isolate Stack\n• 4 Deadlock conditions: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait\n• SJF gives optimal average waiting time",
                "Assuming threads have independent heaps (threads share heap memory).",
                10,
                1
            ),
            (
                "technical",
                "Database Management Systems",
                "ACID Properties, Normalization (1NF to BCNF) & Indexing",
                "dbms-acid-normalization-indexing",
                "Master relational databases, transactions, normal forms, B-Trees vs Hash indexes, and high-frequency interview queries.",
                """
                <h3>ACID Properties of Transactions</h3>
                <div class="grid grid-cols-2 gap-3 my-4">
                    <div class="p-3 bg-blue-50 border border-blue-200 rounded">
                        <strong class="text-blue-900">Atomicity:</strong> All operations succeed, or the transaction is rolled back completely. ('All or Nothing'). Maintained by Transaction Log/Recovery Manager.
                    </div>
                    <div class="p-3 bg-blue-50 border border-blue-200 rounded">
                        <strong class="text-blue-900">Consistency:</strong> Database transitions from one valid state to another, satisfying all schema constraints (keys, triggers).
                    </div>
                    <div class="p-3 bg-blue-50 border border-blue-200 rounded">
                        <strong class="text-blue-900">Isolation:</strong> Concurrent transactions execute without interfering with each other. Maintained by 2-Phase Locking or MVCC.
                    </div>
                    <div class="p-3 bg-blue-50 border border-blue-200 rounded">
                        <strong class="text-blue-900">Durability:</strong> Once committed, changes survive even in case of power loss or system crash. Maintained by Write-Ahead Logging (WAL).
                    </div>
                </div>

                <h3>Database Normalization Cheatsheet</h3>
                <ul class="space-y-2">
                    <li><strong>1NF (First Normal Form):</strong> Each column contains atomic (indivisible) values. No repeating groups or arrays.</li>
                    <li><strong>2NF (Second Normal Form):</strong> In 1NF + <em>No Partial Dependency</em> (Every non-prime attribute must depend on the whole composite candidate key, not just a part of it).</li>
                    <li><strong>3NF (Third Normal Form):</strong> In 2NF + <em>No Transitive Dependency</em> (X → Y where neither X is a superkey nor Y is a prime attribute).</li>
                    <li><strong>BCNF (Boyce-Codd Normal Form):</strong> Stricter than 3NF. For every functional dependency <code>X → Y</code>, <code>X</code> must be a <strong>Super Key</strong>.</li>
                </ul>

                <h3 class="mt-6">Database Indexing: B+ Tree vs Hash Index</h3>
                <p>Most SQL engines use <strong>B+ Trees</strong> for indexing because leaves are linked sequentially, providing <code>O(log N)</code> point lookups AND blazing fast range queries (e.g. <code>WHERE age BETWEEN 20 AND 30</code>). Hash indexes only support exact equality lookups (<code>O(1)</code>) and cannot execute range queries.</p>
                """,
                "• Atomicity, Consistency, Isolation, Durability\n• 1NF: Atomic values\n• 2NF: No partial dependency\n• 3NF: No transitive dependency\n• BCNF: Left side of every dependency must be a superkey\n• B+ Trees handle range queries; Hash indexes do not",
                "Believing an index speeds up write operations (indexes accelerate SELECTs but add overhead to INSERT, UPDATE, DELETE).",
                12,
                2
            ),
            (
                "technical",
                "Computer Networks",
                "OSI Model vs TCP/IP & What happens when you type a URL?",
                "computer-networks-osi-tcp-url",
                "The most asked network interview question explained step-by-step from DNS lookup to TCP 3-way handshake and HTTP/TLS.",
                """
                <h3>Step-by-Step: What happens when you type https://google.com in your browser?</h3>
                <ol class="list-decimal pl-6 space-y-3">
                    <li><strong>1. URL Parsing & Protocol Check:</strong> The browser parses the protocol (<code>https://</code>), domain name (<code>google.com</code>), and default port (<code>443</code>).</li>
                    <li><strong>2. DNS Resolution:</strong>
                        <ul class="list-disc pl-5 mt-1 space-y-1">
                            <li>Browser cache check</li>
                            <li>OS cache check (hosts file / DNS client)</li>
                            <li>Router cache & ISP Recursive Resolver</li>
                            <li>Root DNS Server (.) → TLD Server (.com) → Authoritative Name Server (google.com) returns IP (e.g., <code>142.250.190.46</code>).</li>
                        </ul>
                    </li>
                    <li><strong>3. TCP 3-Way Handshake:</strong>
                        <div class="bg-gray-100 p-3 rounded font-mono text-xs my-2">
                            Client ---- SYN (seq=x) --------> Server<br>
                            Client <--- SYN-ACK (ack=x+1, seq=y) -- Server<br>
                            Client ---- ACK (ack=y+1) ------> Server
                        </div>
                    </li>
                    <li><strong>4. TLS / SSL Handshake:</strong> Client and server exchange cipher suites, verify server certificate against CA root, and derive symmetric session keys.</li>
                    <li><strong>5. HTTP Request & Response:</strong> Browser sends encrypted <code>GET / HTTP/1.1</code>. Server processes request and returns status code (e.g., <code>200 OK</code>) with HTML payload.</li>
                    <li><strong>6. DOM Rendering:</strong> Browser parses HTML to construct DOM tree, parses CSS for CSSOM, builds Render Tree, computes Layout, and Paints pixels on screen.</li>
                </ol>

                <h3 class="mt-6">OSI 7 Layers Quick Memory Trick: 'Please Do Not Throw Sausage Pizza Away'</h3>
                <p>1. Physical -> 2. Data Link -> 3. Network -> 4. Transport -> 5. Session -> 6. Presentation -> 7. Application.</p>
                """,
                "• DNS resolution hierarchy: Browser -> OS -> Resolver -> Root -> TLD -> Authoritative\n• TCP Handshake: SYN -> SYN-ACK -> ACK\n• HTTPS runs over TLS on Port 443; HTTP on Port 80",
                "Confusing TCP (connection-oriented, reliable, flow-controlled) with UDP (connectionless, best-effort, low-latency e.g. DNS/Video streaming).",
                9,
                3
            ),
            (
                "technical",
                "Object Oriented Programming",
                "OOP 4 Pillars & SOLID Principles with Real Examples",
                "oop-pillars-and-solid-principles",
                "Master Encapsulation, Abstraction, Inheritance, Polymorphism and clean architectural SOLID principles.",
                """
                <h3>The 4 Pillars of OOP</h3>
                <div class="grid grid-cols-2 gap-3 my-3">
                    <div class="p-3 bg-purple-50 border border-purple-200 rounded">
                        <strong class="text-purple-900">Encapsulation:</strong> Bundling data (variables) and methods operating on that data into a single unit (class), restricting direct access via access modifiers (private, protected).
                    </div>
                    <div class="p-3 bg-purple-50 border border-purple-200 rounded">
                        <strong class="text-purple-900">Abstraction:</strong> Hiding internal implementation complexities and exposing only essential interfaces (e.g., Abstract classes, Interfaces).
                    </div>
                    <div class="p-3 bg-purple-50 border border-purple-200 rounded">
                        <strong class="text-purple-900">Inheritance:</strong> Mechanism where a new class derives properties and behaviors from an existing parent class (code reusability).
                    </div>
                    <div class="p-3 bg-purple-50 border border-purple-200 rounded">
                        <strong class="text-purple-900">Polymorphism:</strong> Ability of an entity to take multiple forms. Compile-time (Method Overloading) vs Runtime (Method Overriding using virtual tables).
                    </div>
                </div>

                <h3>The SOLID Principles:</h3>
                <ul class="space-y-2 mt-4 text-sm">
                    <li><strong>S - Single Responsibility Principle (SRP):</strong> A class should have one, and only one, reason to change.</li>
                    <li><strong>O - Open/Closed Principle (OCP):</strong> Software entities should be open for extension, but closed for modification.</li>
                    <li><strong>L - Liskov Substitution Principle (LSP):</strong> Subtypes must be substitutable for their base types without altering program correctness.</li>
                    <li><strong>I - Interface Segregation Principle (ISP):</strong> Clients should not be forced to depend upon interfaces they do not use (prefer small, specific interfaces).</li>
                    <li><strong>D - Dependency Inversion Principle (DIP):</strong> High-level modules should not depend on low-level modules; both should depend on abstractions.</li>
                </ul>
                """,
                "• Encapsulation = data hiding\n• Abstraction = interface simplicity\n• Compile-time polymorphism = Overloading\n• Runtime polymorphism = Overriding\n• SOLID: SRP, OCP, LSP, ISP, DIP",
                "Thinking method overloading happens at runtime (overloading is resolved at compile-time by method signature).",
                11,
                4
            ),

            # HR Preparation Modules
            (
                "hr",
                "Behavioral & Frameworks",
                "The STAR Method - Formula for Answering Any HR Question",
                "star-method-framework",
                "Structure your behavioral interview answers to sound confident, structured, and impactful.",
                """
                <h3>What is the STAR Framework?</h3>
                <p>The STAR method is the industry standard framework required by top companies like Amazon, Google, Microsoft, and TCS to evaluate behavioral and situational competency.</p>

                <div class="grid grid-cols-2 gap-4 my-4">
                    <div class="p-4 bg-amber-50 border border-amber-300 rounded">
                        <h4 class="font-bold text-amber-900">S - Situation (15-20% time)</h4>
                        <p class="text-sm mt-1 text-amber-800">Set the scene. Provide specific context: the company, project, timeline, and the specific challenge you faced.</p>
                    </div>
                    <div class="p-4 bg-amber-50 border border-amber-300 rounded">
                        <h4 class="font-bold text-amber-900">T - Task (10-15% time)</h4>
                        <p class="text-sm mt-1 text-amber-800">Identify your exact role and responsibility in that situation. What was required of you specifically?</p>
                    </div>
                    <div class="p-4 bg-amber-50 border border-amber-300 rounded">
                        <h4 class="font-bold text-amber-900">A - Action (50-60% time)</h4>
                        <p class="text-sm mt-1 text-amber-800">The core of your answer! Explain what <strong>YOU</strong> specifically did. What tools, decisions, leadership, or problem-solving did you apply? Say 'I', not 'We'.</p>
                    </div>
                    <div class="p-4 bg-amber-50 border border-amber-300 rounded">
                        <h4 class="font-bold text-amber-900">R - Result (15-20% time)</h4>
                        <p class="text-sm mt-1 text-amber-800">Quantifiable outcome! Mention metrics (e.g. reduced latency by 35%, saved 4 hours/week, scored 94/100, delivered 3 days ahead of deadline).</p>
                    </div>
                </div>

                <h3>Key Rules for HR Success:</h3>
                <ul class="list-disc pl-6 space-y-2 text-sm">
                    <li><strong>Always quantify results:</strong> Numbers stick in the interviewer's memory.</li>
                    <li><strong>Own your actions:</strong> Avoid saying "We decided" — clarify "My specific contribution was...".</li>
                    <li><strong>Keep stories under 2.5 minutes:</strong> Long-winded answers cause interviewers to lose attention.</li>
                </ul>
                """,
                "• S: Situation (Context)\n• T: Task (Your responsibility)\n• A: Action (Specific steps YOU took)\n• R: Result (Quantified metric & learning)",
                "Saying 'we did this' without clarifying your individual contribution.",
                7,
                1
            ),
            (
                "hr",
                "Common HR Questions",
                "Top 10 Frequently Asked HR Questions with Model Answers",
                "top-10-hr-questions-answers",
                "Complete guide with sample answers for 'Tell me about yourself', 'Strengths & Weaknesses', 'Why this company?'.",
                """
                <h3>1. 'Tell me about yourself' (The Elevator Pitch)</h3>
                <p><strong>Formula:</strong> Present (current role/studies) + Past (key achievements/projects) + Future (why you are excited about this role).</p>
                <div class="bg-gray-50 border-l-4 border-emerald-500 p-3 my-2 text-sm italic">
                    "I am currently in my final year of Computer Science at XYZ University with a strong passion for backend systems and algorithms. Over the past two years, I built a scalable real-time chat application handling 5,000 concurrent sockets and interned at ABC where I optimized database queries by 30%. I love solving challenging algorithmic puzzles and have solved over 400 questions on LeetCode. I am excited to interview with your team because your cloud architecture solves high-throughput problems at global scale."
                </div>

                <h3 class="mt-6">2. 'What is your greatest weakness?'</h3>
                <p><strong>Strategy:</strong> Choose a genuine professional weakness (not a cliché like 'I am too perfectionist') and explain the <em>concrete steps you are actively taking</em> to improve.</p>
                <div class="bg-gray-50 border-l-4 border-emerald-500 p-3 my-2 text-sm italic">
                    "Earlier, I used to hesitate asking for help when stuck on a bug, spending hours trying to solve it alone. I realized this affects team velocity. Now, I follow the 30-minute rule: if I make no progress after 30 minutes of deep debugging and checking documentation, I frame a concise question with my tried hypotheses and seek a senior's guidance."
                </div>

                <h3 class="mt-6">3. 'Why should we hire you over other candidates?'</h3>
                <p><strong>Strategy:</strong> Align your proven skills with their exact job requirements, highlight your rapid learning ability, and show cultural enthusiasm.</p>
                """,
                "• Tell me about yourself: Present -> Past -> Future (under 90 seconds)\n• Weakness: Genuine skill + active mitigation system\n• Why us: Research specific products/values of the company",
                "Reciting your resume verbatim during 'Tell me about yourself'.",
                8,
                2
            )
        ]

        cursor.executemany('''
            INSERT INTO prep_modules (
                category, subcategory, title, slug, summary, content_html,
                key_formulas_or_points, common_mistakes, read_time_mins, order_index
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', prep_modules_data)

        print("Seeding Practice Quizzes...")
        quiz_data = [
            # Aptitude Quizzes
            (
                "aptitude",
                "Time and Work",
                "A can complete a piece of work in 12 days and B can complete it in 18 days. They worked together for 4 days, after which B left. How many more days will A take to complete the remaining work?",
                "4 days",
                "5 days",
                "6 days",
                "5.33 days (16/3 days)",
                "D",
                "Total Work = LCM(12, 18) = 36 units. Efficiency of A = 36/12 = 3 units/day. Efficiency of B = 36/18 = 2 units/day. In 4 days, together they complete: 4 × (3 + 2) = 20 units. Remaining work = 36 - 20 = 16 units. Time taken by A alone = 16 / 3 = 5.33 days.",
                "Medium"
            ),
            (
                "aptitude",
                "Speed, Time & Distance",
                "A train 150 meters long passes a telegraph pole in 10 seconds. In what time will it pass a bridge of length 300 meters?",
                "20 seconds",
                "25 seconds",
                "30 seconds",
                "35 seconds",
                "C",
                "Speed of train = Length of train / Time = 150 m / 10 s = 15 m/s. When passing a bridge, total distance = Length of train + Length of bridge = 150 + 300 = 450 meters. Time taken = 450 m / 15 m/s = 30 seconds.",
                "Easy"
            ),
            (
                "aptitude",
                "Percentages",
                "If the price of petrol increases by 25%, by what percentage must a car owner reduce fuel consumption so that the overall expenditure remains unchanged?",
                "20%",
                "25%",
                "16.67%",
                "15%",
                "A",
                "Formula: Reduction % = [r / (100 + r)] × 100%. Here r = 25%. Reduction = [25 / 125] × 100% = 1/5 × 100% = 20%.",
                "Easy"
            ),
            (
                "aptitude",
                "Profit and Loss",
                "A shopkeeper sells an article at a 15% discount on the marked price and still earns a profit of 19%. By how much percent was the article marked up above the cost price?",
                "34%",
                "40%",
                "36%",
                "45%",
                "B",
                "Let CP = 100. Then SP = 100 + 19 = 119. Since SP is 85% of Marked Price (MP), 0.85 × MP = 119 => MP = 119 / 0.85 = 140. Markup = 140 - 100 = 40%.",
                "Medium"
            ),
            (
                "aptitude",
                "Logical Reasoning",
                "Statements: 1. All apples are fruits. 2. Some fruits are sweet.\nConclusions:\nI. Some apples are sweet.\nII. No apple is sweet.",
                "Only I follows",
                "Only II follows",
                "Either I or II follows",
                "Neither I nor II follows",
                "C",
                "The terms 'sweet' and 'apples' form a complementary pair ('Some' and 'No') with identical subject and predicate. Neither conclusion can be definitively proven from the premises, but one of them must necessarily be true. Hence, either I or II follows.",
                "Medium"
            ),
            
            # Technical Core Quizzes
            (
                "technical",
                "Operating Systems",
                "Which CPU scheduling algorithm is non-preemptive and provides the minimum average waiting time among all non-preemptive algorithms for a given set of processes?",
                "Round Robin",
                "First-Come, First-Served (FCFS)",
                "Shortest Job First (SJF)",
                "Priority Scheduling",
                "C",
                "Shortest Job First (SJF) is mathematically proven to be optimal in terms of minimizing average waiting time for a set of stationary processes because scheduling the shortest job first moves processes through the waiting queue fastest.",
                "Easy"
            ),
            (
                "technical",
                "Database Management Systems",
                "Consider a relation R(A, B, C, D) with candidate key AB. Which of the following functional dependencies violates 2NF (Second Normal Form)?",
                "AB -> C",
                "A -> C",
                "AB -> D",
                "C -> D",
                "B",
                "Second Normal Form (2NF) strictly forbids Partial Dependency, where a non-prime attribute depends on a proper subset of any candidate key. In A -> C, C depends only on A (part of candidate key AB), violating 2NF.",
                "Medium"
            ),
            (
                "technical",
                "Computer Networks",
                "During a TCP 3-way handshake, if the client sends SYN with sequence number 500, what will be the acknowledgment number (ACK) sent back by the server in the SYN-ACK segment?",
                "500",
                "501",
                "0",
                "1",
                "B",
                "In TCP, the acknowledgment number indicates the NEXT sequence number the receiver expects to receive. Since the SYN flag consumes 1 sequence number, the server acknowledges with ACK = client_seq + 1 = 500 + 1 = 501.",
                "Medium"
            ),
            (
                "technical",
                "Object Oriented Programming",
                "Which design principle states that 'High-level modules should not depend on low-level modules; both should depend on abstractions'?",
                "Liskov Substitution Principle",
                "Single Responsibility Principle",
                "Dependency Inversion Principle",
                "Open/Closed Principle",
                "C",
                "The Dependency Inversion Principle (the 'D' in SOLID) mandates that software should decouple high-level policy code from low-level implementation details by introducing abstract interfaces.",
                "Easy"
            )
        ]

        cursor.executemany('''
            INSERT INTO quiz_questions (
                category, subtopic, question_text, option_a, option_b,
                option_c, option_d, correct_option, explanation, difficulty
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', quiz_data)

        print("Seeding Dedicated Topic-wise DSA SDE Sheet Problems...")
        dsa_sheet_data = [
            # Topic: Arrays
            (
                "Arrays",
                "Basic & Hashing",
                "Two Sum",
                "two-sum",
                "Easy",
                "https://leetcode.com/problems/two-sum/",
                "https://www.geeksforgeeks.org/check-if-pair-with-given-sum-exists-in-array/",
                "Amazon, Google, Microsoft, Meta, Apple",
                "Given an array of integers <code>nums</code> and an integer <code>target</code>, return indices of the two numbers such that they add up to target.\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.",
                "2 <= nums.length <= 10^4\n-10^9 <= nums[i] <= 10^9\n-10^9 <= target <= 10^9",
                "Can you use a Hash Map to store previously seen numbers and their indices in O(1) lookup?",
                "Use a hash map. For each number x, check if (target - x) already exists in the map. If yes, return current index and map[target - x]. Otherwise, record map[x] = current index.",
                "O(N)",
                "O(N)",
                """def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []""",
                """#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;
    for (int i = 0; i < nums.size(); i++) {
        int comp = target - nums[i];
        if (seen.find(comp) != seen.end()) {
            return {seen[comp], i};
        }
        seen[nums[i]] = i;
    }
    return {};
}""",
                """import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];
            if (seen.containsKey(comp)) {
                return new int[] { seen.get(comp), i };
            }
            seen.put(nums[i], i);
        }
        return new int[0];
    }
}""",
                1
            ),
            (
                "Arrays",
                "Kadane's Algorithm",
                "Maximum Subarray Sum (Kadane's Algorithm)",
                "maximum-subarray-kadanes",
                "Medium",
                "https://leetcode.com/problems/maximum-subarray/",
                "https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/",
                "Amazon, Microsoft, TCS, Infosys, Adobe",
                "Given an integer array <code>nums</code>, find the subarray with the largest sum, and return its sum.",
                "1 <= nums.length <= 10^5\n-10^4 <= nums[i] <= 10^4",
                "If current running sum becomes negative, is it beneficial to carry it forward to subsequent elements?",
                "Maintain a current_sum and max_sum. Add current element to current_sum. If current_sum exceeds max_sum, update max_sum. If current_sum drops below 0, reset current_sum = 0.",
                "O(N)",
                "O(1)",
                """def maxSubArray(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for num in nums:
        curr_sum += num
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum""",
                """#include <vector>
#include <algorithm>
using namespace std;

int maxSubArray(vector<int>& nums) {
    int maxSum = nums[0];
    int currSum = 0;
    for (int x : nums) {
        currSum += x;
        maxSum = max(maxSum, currSum);
        if (currSum < 0) currSum = 0;
    }
    return maxSum;
}""",
                """public class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currSum = 0;
        for (int x : nums) {
            currSum += x;
            if (currSum > maxSum) maxSum = currSum;
            if (currSum < 0) currSum = 0;
        }
        return maxSum;
    }
}""",
                2
            ),
            (
                "Arrays",
                "Dutch National Flag",
                "Sort Colors (Sort 0s, 1s, and 2s)",
                "sort-colors-0-1-2",
                "Medium",
                "https://leetcode.com/problems/sort-colors/",
                "https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/",
                "Amazon, Microsoft, Paytm, Walmart",
                "Given an array <code>nums</code> with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with colors 0, 1, and 2.",
                "n == nums.length\n1 <= n <= 300\nnums[i] is either 0, 1, or 2.",
                "Use 3 pointers: low, mid, and high.",
                "Dutch National Flag algorithm: low points to end of 0s, mid scans through elements, high points to start of 2s. If nums[mid] == 0: swap(low, mid), low++, mid++. If nums[mid] == 1: mid++. If nums[mid] == 2: swap(mid, high), high--.",
                "O(N)",
                "O(1)",
                """def sortColors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else: # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1""",
                """#include <vector>
#include <algorithm>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0, mid = 0, high = nums.size() - 1;
    while (mid <= high) {
        if (nums[mid] == 0) swap(nums[low++], nums[mid++]);
        else if (nums[mid] == 1) mid++;
        else swap(nums[mid], nums[high--]);
    }
}""",
                """public class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                int temp = nums[low]; nums[low] = nums[mid]; nums[mid] = temp;
                low++; mid++;
            } else if (nums[mid] == 1) {
                mid++;
            } else {
                int temp = nums[mid]; nums[mid] = nums[high]; nums[high] = temp;
                high--;
            }
        }
    }
}""",
                3
            ),
            (
                "Arrays",
                "Array Traversal",
                "Best Time to Buy and Sell Stock",
                "best-time-to-buy-and-sell-stock",
                "Easy",
                "https://leetcode.com/problems/best-time-to-buy-and-sell-stock/",
                "https://www.geeksforgeeks.org/best-time-to-buy-and-sell-stock/",
                "Google, Amazon, Microsoft, Uber, Goldman Sachs",
                "You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the i-th day.\nYou want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.",
                "1 <= prices.length <= 10^5\n0 <= prices[i] <= 10^4",
                "Keep track of the minimum buying price seen so far as you iterate through the list.",
                "Track min_price encountered so far. On day i, potential profit = prices[i] - min_price. Keep max profit updated.",
                "O(N)",
                "O(1)",
                """def maxProfit(prices: list[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit""",
                """#include <vector>
#include <algorithm>
using namespace std;

int maxProfit(vector<int>& prices) {
    int minPrice = 1e9, maxProf = 0;
    for (int p : prices) {
        minPrice = min(minPrice, p);
        maxProf = max(maxProf, p - minPrice);
    }
    return maxProf;
}""",
                """public class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE, maxProfit = 0;
        for (int p : prices) {
            if (p < minPrice) minPrice = p;
            else if (p - minPrice > maxProfit) maxProfit = p - minPrice;
        }
        return maxProfit;
    }
}""",
                4
            ),

            # Topic: Two Pointers & Sliding Window
            (
                "Two Pointers",
                "Two Pointers",
                "Trapping Rain Water",
                "trapping-rain-water",
                "Hard",
                "https://leetcode.com/problems/trapping-rain-water/",
                "https://www.geeksforgeeks.org/trapping-rain-water/",
                "Google, Amazon, Microsoft, Goldman Sachs, Bloomberg",
                "Given <code>n</code> non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.",
                "n == height.length\n1 <= n <= 2 * 10^4\n0 <= height[i] <= 10^5",
                "Water trapped above bar i is determined by min(max_left, max_right) - height[i].",
                "Use two pointers (left=0, right=n-1) with left_max and right_max. Whichever side is smaller determines the bottleneck and can be resolved immediately.",
                "O(N)",
                "O(1)",
                """def trap(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    while left < right:
        if height[left] <= height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water""",
                """#include <vector>
#include <algorithm>
using namespace std;

int trap(vector<int>& height) {
    int left = 0, right = height.size() - 1;
    int leftMax = 0, rightMax = 0, water = 0;
    while (left < right) {
        if (height[left] <= height[right]) {
            if (height[left] >= leftMax) leftMax = height[left];
            else water += leftMax - height[left];
            left++;
        } else {
            if (height[right] >= rightMax) rightMax = height[right];
            else water += rightMax - height[right];
            right--;
        }
    }
    return water;
}""",
                """public class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1;
        int leftMax = 0, rightMax = 0, water = 0;
        while (left < right) {
            if (height[left] <= height[right]) {
                if (height[left] >= leftMax) leftMax = height[left];
                else water += leftMax - height[left];
                left++;
            } else {
                if (height[right] >= rightMax) rightMax = height[right];
                else water += rightMax - height[right];
                right--;
            }
        }
        return water;
    }
}""",
                5
            ),
            (
                "Sliding Window",
                "Substring",
                "Longest Substring Without Repeating Characters",
                "longest-substring-without-repeating-characters",
                "Medium",
                "https://leetcode.com/problems/longest-substring-without-repeating-characters/",
                "https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/",
                "Amazon, Microsoft, Google, Meta, Apple",
                "Given a string <code>s</code>, find the length of the longest substring without repeating characters.",
                "0 <= s.length <= 5 * 10^4\ns consists of English letters, digits, symbols and spaces.",
                "Maintain a sliding window [left, right] and a hash map of character positions.",
                "Expand window with right pointer. When duplicate char s[right] is found at pos >= left, jump left = pos + 1. Update max_length.",
                "O(N)",
                "O(min(M, N))",
                """def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len""",
                """#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int lengthOfLongestSubstring(string s) {
    vector<int> lastIndex(256, -1);
    int left = 0, maxLen = 0;
    for (int right = 0; right < s.length(); right++) {
        if (lastIndex[s[right]] >= left) {
            left = lastIndex[s[right]] + 1;
        }
        lastIndex[s[right]] = right;
        maxLen = max(maxLen, right - left + 1);
    }
    return maxLen;
}""",
                """import java.util.HashMap;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        int left = 0, maxLen = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            if (map.containsKey(c) && map.get(c) >= left) {
                left = map.get(c) + 1;
            }
            map.put(c, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }
        return maxLen;
    }
}""",
                6
            ),

            # Topic: Linked List
            (
                "Linked List",
                "Reversal",
                "Reverse a Linked List",
                "reverse-linked-list",
                "Easy",
                "https://leetcode.com/problems/reverse-linked-list/",
                "https://www.geeksforgeeks.org/reverse-a-linked-list/",
                "Amazon, Microsoft, Google, TCS, Cognizant",
                "Given the head of a singly linked list, reverse the list, and return the reversed list.",
                "Number of nodes in the list is the range [0, 5000].\n-5000 <= Node.val <= 5000",
                "Iterative method requires 3 pointers: prev, curr, next_node.",
                "Initialize prev = null, curr = head. In a loop, save next_node = curr.next, point curr.next = prev, move prev = curr, curr = next_node. Return prev.",
                "O(N)",
                "O(1)",
                """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev""",
                """struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* curr = head;
    while (curr) {
        ListNode* nxt = curr->next;
        curr->next = prev;
        prev = curr;
        curr = nxt;
    }
    return prev;
}""",
                """public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}""",
                7
            ),
            (
                "Linked List",
                "Cycle Detection",
                "Linked List Cycle II (Find Start of Cycle)",
                "linked-list-cycle-ii",
                "Medium",
                "https://leetcode.com/problems/linked-list-cycle-ii/",
                "https://www.geeksforgeeks.org/find-first-node-of-loop-in-a-linked-list/",
                "Amazon, Microsoft, Google, Oracle",
                "Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.",
                "Number of nodes is in range [0, 10^4].",
                "Floyd's Tortoise and Hare algorithm.",
                "Move slow by 1 step, fast by 2 steps. When they meet, reset slow to head. Move both slow and fast 1 step at a time; their meeting point is the cycle start.",
                "O(N)",
                "O(1)",
                """def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None""",
                """ListNode *detectCycle(ListNode *head) {
    ListNode *slow = head, *fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            slow = head;
            while (slow != fast) {
                slow = slow->next;
                fast = fast->next;
            }
            return slow;
        }
    }
    return nullptr;
}""",
                """public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                slow = head;
                while (slow != fast) {
                    slow = slow.next;
                    fast = fast.next;
                }
                return slow;
            }
        }
        return null;
    }
}""",
                8
            ),

            # Topic: Binary Search
            (
                "Binary Search",
                "Rotated Array",
                "Search in Rotated Sorted Array",
                "search-in-rotated-sorted-array",
                "Medium",
                "https://leetcode.com/problems/search-in-rotated-sorted-array/",
                "https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/",
                "Google, Microsoft, Amazon, Meta, Flipkart",
                "Given an integer array <code>nums</code> sorted in ascending order (with distinct values) that is possibly rotated at an unknown pivot, search for <code>target</code>. Return its index, or -1 if not present.",
                "1 <= nums.length <= 5000\n-10^4 <= nums[i] <= 10^4",
                "At least one half of the array [low, mid] or [mid, high] is always normally sorted.",
                "Compute mid. Check if nums[mid] == target. If nums[low] <= nums[mid], left half is sorted: check if target is between nums[low] and nums[mid]. Otherwise right half is sorted.",
                "O(log N)",
                "O(1)",
                """def search(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        # Check if left half is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else: # Right half is sorted
            if nums[mid] < target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1""",
                """#include <vector>
using namespace std;

int search(vector<int>& nums, int target) {
    int low = 0, high = nums.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) return mid;
        if (nums[low] <= nums[mid]) {
            if (nums[low] <= target && target < nums[mid]) high = mid - 1;
            else low = mid + 1;
        } else {
            if (nums[mid] < target && target <= nums[high]) low = mid + 1;
            else high = mid - 1;
        }
    }
    return -1;
}""",
                """public class Solution {
    public int search(int[] nums, int target) {
        int low = 0, high = nums.length - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) return mid;
            if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) high = mid - 1;
                else low = mid + 1;
            } else {
                if (nums[mid] < target && target <= nums[high]) low = mid + 1;
                else high = mid - 1;
            }
        }
        return -1;
    }
}""",
                9
            ),

            # Topic: Trees & BST
            (
                "Trees",
                "Tree Traversal",
                "Lowest Common Ancestor of a Binary Tree",
                "lowest-common-ancestor-binary-tree",
                "Medium",
                "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/",
                "https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/",
                "Amazon, Microsoft, Google, Meta, Apple",
                "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes <code>p</code> and <code>q</code>.",
                "Number of nodes is in range [2, 10^5]. All node values are unique.",
                "Use recursive post-order DFS traversal.",
                "If root is null or root == p or root == q, return root. Recurse left and right. If both return non-null, root is LCA. If only one returns non-null, propagate that non-null node up.",
                "O(N)",
                "O(H) where H is tree height",
                """def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right""",
                """TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
    if (!root || root == p || root == q) return root;
    TreeNode* left = lowestCommonAncestor(root->left, p, q);
    TreeNode* right = lowestCommonAncestor(root->right, p, q);
    if (left && right) return root;
    return left ? left : right;
}""",
                """public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }
}""",
                10
            ),
            (
                "Trees",
                "Tree Construction",
                "Binary Tree Level Order Traversal",
                "binary-tree-level-order-traversal",
                "Medium",
                "https://leetcode.com/problems/binary-tree-level-order-traversal/",
                "https://www.geeksforgeeks.org/level-order-tree-traversal/",
                "Amazon, Microsoft, Bloomberg, TCS Digital",
                "Given the root of a binary tree, return the level order traversal of its nodes' values (i.e., from left to right, level by level).",
                "Number of nodes is in range [0, 2000].",
                "Use a Queue (BFS) with level size tracking.",
                "Push root to queue. While queue is not empty, get current queue size `sz`. Pop `sz` elements for this level, appending their values to level list and pushing children to queue.",
                "O(N)",
                "O(N)",
                """from collections import deque

def levelOrder(root) -> list[list[int]]:
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level)
    return res""",
                """#include <vector>
#include <queue>
using namespace std;

vector<vector<int>> levelOrder(TreeNode* root) {
    if (!root) return {};
    vector<vector<int>> res;
    queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        for (int i = 0; i < sz; i++) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        res.push_back(level);
    }
    return res;
}""",
                """import java.util.*;

public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            int sz = q.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < sz; i++) {
                TreeNode node = q.poll();
                level.add(node.val);
                if (node.left != null) q.add(node.left);
                if (node.right != null) q.add(node.right);
            }
            res.add(level);
        }
        return res;
    }
}""",
                11
            ),

            # Topic: Graphs
            (
                "Graphs",
                "Traversal & BFS",
                "Number of Islands",
                "number-of-islands",
                "Medium",
                "https://leetcode.com/problems/number-of-islands/",
                "https://www.geeksforgeeks.org/find-number-of-islands/",
                "Amazon, Google, Microsoft, Meta, Bloomberg",
                "Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of '1's (land) and '0's (water), return the number of islands.\nAn island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.",
                "m == grid.length\nn == grid[i].length\n1 <= m, n <= 300\ngrid[i][j] is '0' or '1'.",
                "Traverse every cell. When you find '1', trigger DFS or BFS to sink all connected '1's into '0's and increment counter.",
                "Iterate through all grid cells. If cell is '1', increment island count and run DFS to mark all 4-directionally adjacent '1's as '0' (visited).",
                "O(M * N)",
                "O(M * N) recursion stack",
                """def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return
        grid[r][c] = '0' # mark visited
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                islands += 1
                dfs(i, j)
    return islands""",
                """#include <vector>
using namespace std;

void dfs(vector<vector<char>>& grid, int r, int c) {
    if (r < 0 || r >= grid.size() || c < 0 || c >= grid[0].size() || grid[r][c] != '1') return;
    grid[r][c] = '0';
    dfs(grid, r + 1, c);
    dfs(grid, r - 1, c);
    dfs(grid, r, c + 1);
    dfs(grid, r, c - 1);
}

int numIslands(vector<vector<char>>& grid) {
    int count = 0;
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '1') {
                count++;
                dfs(grid, i, j);
            }
        }
    }
    return count;
}""",
                """public class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }
    private void dfs(char[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || grid[r][c] != '1') return;
        grid[r][c] = '0';
        dfs(grid, r + 1, c);
        dfs(grid, r - 1, c);
        dfs(grid, r, c + 1);
        dfs(grid, r, c - 1);
    }
}""",
                12
            ),
            (
                "Graphs",
                "Topological Sort",
                "Course Schedule (Cycle Detection in Directed Graph)",
                "course-schedule",
                "Medium",
                "https://leetcode.com/problems/course-schedule/",
                "https://www.geeksforgeeks.org/detect-cycle-in-a-directed-graph-using-bfs-kahns-algorithm/",
                "Amazon, Google, Microsoft, Twitter, Uber",
                "There are a total of <code>numCourses</code> courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [a, b] indicates you must take course b first if you want to take a.\nReturn true if you can finish all courses.",
                "1 <= numCourses <= 2000\n0 <= prerequisites.length <= 5000",
                "Use Kahn's Algorithm (BFS topological sort with in-degrees) or DFS with recursion stack array.",
                "Compute in-degrees for each vertex. Push all vertices with in-degree 0 into a queue. Process nodes: for each neighbor, decrement in-degree; if 0, push to queue. If processed nodes == numCourses, no cycle exists.",
                "O(V + E)",
                "O(V + E)",
                """from collections import deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    adj = {i: [] for i in range(numCourses)}
    indegree = [0] * numCourses
    for dest, src in prerequisites:
        adj[src].append(dest)
        indegree[dest] += 1
        
    q = deque([i for i in range(numCourses) if indegree[i] == 0])
    count = 0
    while q:
        node = q.popleft()
        count += 1
        for neighbor in adj[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)
    return count == numCourses""",
                """#include <vector>
#include <queue>
using namespace std;

bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
    vector<vector<int>> adj(numCourses);
    vector<int> indegree(numCourses, 0);
    for (auto& p : prerequisites) {
        adj[p[1]].push_back(p[0]);
        indegree[p[0]]++;
    }
    queue<int> q;
    for (int i = 0; i < numCourses; i++) {
        if (indegree[i] == 0) q.push(i);
    }
    int visited = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        visited++;
        for (int v : adj[u]) {
            if (--indegree[v] == 0) q.push(v);
        }
    }
    return visited == numCourses;
}""",
                """import java.util.*;

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) adj.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] p : prerequisites) {
            adj.get(p[1]).add(p[0]);
            indegree[p[0]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegree[i] == 0) q.add(i);
        }
        int count = 0;
        while (!q.isEmpty()) {
            int u = q.poll();
            count++;
            for (int v : adj.get(u)) {
                if (--indegree[v] == 0) q.add(v);
            }
        }
        return count == numCourses;
    }
}""",
                13
            ),

            # Topic: Dynamic Programming
            (
                "Dynamic Programming",
                "1D DP",
                "Climbing Stairs",
                "climbing-stairs",
                "Easy",
                "https://leetcode.com/problems/climbing-stairs/",
                "https://www.geeksforgeeks.org/count-ways-reach-nth-stair/",
                "Amazon, TCS, Infosys, Adobe, Apple",
                "You are climbing a staircase. It takes <code>n</code> steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
                "1 <= n <= 45",
                "To reach step n, you must come from step (n-1) or step (n-2).",
                "State transition: dp[i] = dp[i-1] + dp[i-2], identical to Fibonacci. Space can be optimized to O(1) by keeping just the last two values.",
                "O(N)",
                "O(1)",
                """def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second""",
                """int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}""",
                """public class Solution {
    public int climbStairs(int n) {
        if (n <= 2) return n;
        int a = 1, b = 2;
        for (int i = 3; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }
}""",
                14
            ),
            (
                "Dynamic Programming",
                "Knapsack & Subsequences",
                "Coin Change (Minimum Coins)",
                "coin-change",
                "Medium",
                "https://leetcode.com/problems/coin-change/",
                "https://www.geeksforgeeks.org/coin-change-dp-7/",
                "Amazon, Microsoft, Google, Goldman Sachs, Paytm",
                "You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code>.\nReturn the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up, return -1.",
                "1 <= coins.length <= 12\n1 <= coins[i] <= 2^31 - 1\n0 <= amount <= 10^4",
                "Let dp[i] be the minimum coins to make amount i.",
                "Initialize dp array of size (amount + 1) filled with infinity, dp[0] = 0. For each amount from 1 to amount, for each coin in coins: if amount >= coin, dp[amount] = min(dp[amount], 1 + dp[amount - coin]).",
                "O(amount * len(coins))",
                "O(amount)",
                """def coinChange(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], 1 + dp[x - coin])
    return dp[amount] if dp[amount] != float('inf') else -1""",
                """#include <vector>
#include <algorithm>
using namespace std;

int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, 1e9);
    dp[0] = 0;
    for (int c : coins) {
        for (int x = c; x <= amount; x++) {
            dp[x] = min(dp[x], 1 + dp[x - c]);
        }
    }
    return dp[amount] >= 1e9 ? -1 : dp[amount];
}""",
                """import java.util.Arrays;

public class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int c : coins) {
            for (int x = c; x <= amount; x++) {
                dp[x] = Math.min(dp[x], 1 + dp[x - c]);
            }
        }
        return dp[amount] > amount ? -1 : dp[amount];
    }
}""",
                15
            ),
            (
                "Dynamic Programming",
                "Longest Common Subsequence",
                "Longest Common Subsequence (LCS)",
                "longest-common-subsequence",
                "Medium",
                "https://leetcode.com/problems/longest-common-subsequence/",
                "https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/",
                "Amazon, Microsoft, Google, PayPal",
                "Given two strings <code>text1</code> and <code>text2</code>, return the length of their longest common subsequence. If there is no common subsequence, return 0.",
                "1 <= text1.length, text2.length <= 1000",
                "2D grid dp[i][j]: if text1[i-1] == text2[j-1], dp[i][j] = 1 + dp[i-1][j-1].",
                "Build (m+1) x (n+1) DP table. If characters match, take diagonal + 1. Otherwise take max(dp[i-1][j], dp[i][j-1]).",
                "O(M * N)",
                "O(M * N)",
                """def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]""",
                """#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int longestCommonSubsequence(string text1, string text2) {
    int m = text1.size(), n = text2.size();
    vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            if (text1[i - 1] == text2[j - 1]) dp[i][j] = 1 + dp[i - 1][j - 1];
            else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }
    return dp[m][n];
}""",
                """public class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (text1.charAt(i - 1) == text2.charAt(j - 1)) {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }
}""",
                16
            )
        ]

        cursor.executemany('''
            INSERT INTO dsa_problems (
                topic, subtopic, title, slug, difficulty, leetcode_url, gfg_url,
                company_tags, problem_statement, constraints, hints, solution_approach,
                time_complexity, space_complexity, solution_python, solution_cpp, solution_java,
                order_index
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', dsa_sheet_data)

        conn.commit()
        print("Database successfully seeded with comprehensive real-world content!")

if __name__ == '__main__':
    seed_all()
