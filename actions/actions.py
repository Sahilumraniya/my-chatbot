from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

# --- Data Extracted from your JavaScript ---
# Convert your JS arrays of objects into Python dictionaries for easy lookup
# Keys are lowercased for case-insensitive matching

PROJECT_DATA = {
    "swap & share": {
        "title": "Swap & Share",
        "description": "A full-stack web application for trading and sharing items. It includes features like user authentication, listings, and real-time communication. Built with React JS, Tailwind CSS, NodeJs, MongoDB, AWS S3, and Express.",
        "github": "https://github.com/Sahilumraniya/ShwapNShare/",
        "host": "https://swapnshare.vercel.app/",
        "tech": ["React JS", "Tailwind CSS", "NodeJs", "MongoDB", "AWS S3", "Express"],
        "tag": "web",
    },
    "ai maze solver": {
        "title": "AI maze solver",
        "description": "A Python-based AI project that solves mazes using various AI algorithms. It's built with Python and Pygame.",
        "github": "https://github.com/Sahilumraniya/Maze_Game",
        "host": "https://drive.google.com/file/d/1LrzyO_xEnLR_5kf07WBCzsCL-b5WsLQg/view",
        "tech": ["Python", "Pygame", "AI"],
        "tag": "python",
    },
    "learnfinity": {
        "title": "Learnfinity",
        "description": "An online learning platform. Developed with Next JS, Tailwind CSS, and React JS.",
        "github": "https://github.com/Sahilumraniya/Learnfinity",
        "host": "https://learnfinity.vercel.app/",
        "tech": ["Next JS", "Tailwind CSS", "React JS"],
        "tag": "web",
    },
    "manufacturing business website": {
        "title": "Manufacturing Business Website",
        "description": "A responsive website for a manufacturing business. Built using Next JS, Tailwind CSS, and React JS.",
        "github": "https://github.com/Sahilumraniya/Bhramani-Machinery",
        "host": "https://bhramani-machinery.vercel.app/",
        "tech": ["Next JS", "Tailwind CSS", "React JS"],
        "tag": "web",
    },
    "startup-directory-web-app": {
        "title": "Startup-Directory-Web-App",
        "description": "A web application for listing and managing startup directories. Technologies include React JS, Tailwind CSS, Node Js, MongoDB, and Express Js.",
        "github": "https://github.com/Sahilumraniya/Startup-Directory-Web-App",
        "host": "https://startup-directory-web-app.vercel.app/",
        "tech": ["React JS", "Tailwind CSS", "Node Js", "MongoDB", "Express Js"],
        "tag": "web",
    },
    "flappy bird game": {
        "title": "Flappy Bird Game",
        "description": "A classic Flappy Bird game developed using Python and Pygame.",
        "github": "https://github.com/Sahilumraniya/Flappy-Bird-Game",
        "host": "https://github.com/Sahilumraniya/Flappy-Bird-Game/releases/tag/v1.0",
        "tech": ["python", "pygame"],
        "tag": "python",
    },
    "expense manager flutter app": {
        "title": "Expense manager Flutter App",
        "description": "A mobile application for managing expenses, built with Flutter and Dart for Android devices.",
        "github": "https://github.com/Sahilumraniya/Expense-manager-Flutter-App",
        "host": "https://github.com/Sahilumraniya/Expense-manager-Flutter-App", # Host points to github repo
        "tech": ["Flutter", "Dart", "Android"],
        "tag": "Mobile Application"
    },
    "movie search": {
        "title": "Movie Search",
        "description": "A web application for searching movies. Uses HTML 5, CSS 3, and JavaScript.",
        "github": "https://github.com/sahilumraniya/MovieSearch/",
        "host": "https://sahilumraniya.github.io/MovieSearch/",
        "tech": ["HTML 5", "CSS 3", "JavaScript"],
        "tag": "web",
    },
    "insightful-blog": {
        "title": "Insightful-Blog",
        "description": "A blogging platform for sharing insightful articles. Built with HTML 5, CSS 3, and JavaScript.",
        "github": "https://github.com/Sahilumraniya/Insightful-Blog",
        "host": "https://sahilumraniya.github.io/Insightful-Blog/",
        "tech": ["HTML 5", "CSS 3", "JavaScript"],
        "tag": "web",
    }
}

SKILL_DATA = {
    "javascript": "JavaScript: Proficient in both frontend (React) and backend (Node.js/Express.js) development, building dynamic and interactive web applications.",
    "typescript": "TypeScript: Experienced in using TypeScript for building scalable and type-safe applications.",
    "next js": "Next JS: Skilled in building modern web applications with Next.js for server-side rendering and static site generation.",
    "react js": "React JS: Experienced in building modern single-page applications with React, focusing on component-based architecture and state management.",
    "tailwind css": "Tailwind CSS: Proficient in rapidly building custom user interfaces with Tailwind CSS.",
    "bootstrap": "Bootstrap: Experienced in using Bootstrap for responsive and mobile-first frontend development.",
    "node js": "Node JS: Skilled in developing scalable backend services and APIs using Node.js.",
    "mongodb": "MongoDB: Familiar with NoSQL databases like MongoDB for flexible data storage and retrieval in web applications.",
    "my sql": "My SQL: Experienced in relational database management using MySQL.",
    "postgresql": "PostgreSQL: Proficient in relational databases like PostgreSQL, including schema design, complex queries, and database optimization.",
    "docker": "Docker: Experienced in containerization using Docker for consistent development and deployment environments.",
    "git": "Git: Proficient in version control using Git, including collaborative workflows.",
    "feathers": "Feathers.js: Experienced in developing real-time applications and RESTful APIs using Feathers.js.",
    "c": "C: Solid understanding of programming fundamentals and data structures using C.",
    "c++": "C++: Proficient in C++ for competitive programming and system-level applications.",
    "python": "Python: Extensive experience with Python, including web development (Django/Flask), data processing (NumPy, Pandas), and scripting (Pygame).",
    "java": "Java: Strong grasp of Java for object-oriented programming and application development.",
    "express.js": "Express.js: Built efficient and scalable RESTful APIs with Express.js, integrating with various databases and third-party services.",
    "spring boot": "Spring Boot: Experienced in developing robust backend applications using the Spring Boot framework.",
    "numpy": "NumPy: Utilized NumPy for numerical computing and array operations in data science projects.",
    "pandas": "Pandas: Proficient in data manipulation and analysis using Pandas.",
    "matplotlib": "Matplotlib: Experienced in data visualization and plotting using Matplotlib.",
    "scikit-learn": "Scikit-learn: Applied Scikit-learn for various machine learning tasks, including classification and regression.",
    "tableau": "Tableau: Used Tableau for creating interactive data visualizations and business intelligence dashboards.",
    "pygame": "Pygame: Developed games and interactive applications using the Pygame library in Python.",
    "html 5": "HTML 5: Expert in structuring web content with HTML5.",
    "css 3": "CSS 3: Proficient in styling web pages with advanced CSS3 techniques.",
    "dart": "Dart: Experienced in developing cross-platform applications with Dart, primarily for Flutter.",
    "android": "Android: Skilled in building native Android applications.",
    "flutter": "Flutter: Proficient in cross-platform mobile app development using Flutter.",
    "kotlin": "Kotlin: Basic understanding and experience with Kotlin for Android development.",
    "oracle cloud infrastructure": "Oracle Cloud Infrastructure: Certified in deploying and optimizing generative AI solutions on OCI.",
    "sap": "SAP: Achieved certification in Machine Learning & IoT training under the SAP Code Unnati Program.",
    "advancejava": "Advance Java: Completed an Advanced Java course, focusing on complex programming concepts and Java application development.",
}

ACHIEVEMENT_DATA = {
    "oracle cloud infrastructure 2024 generative ai certified professional": {
        "title": "Oracle Cloud Infrastructure 2024 Generative AI Certified Professional",
        "organization": "Oracle",
        "details": "Participated in training on deploying and optimizing generative AI solutions using Oracle Cloud Infrastructure.",
        "date": "July 17, 2024",
        "link": "https://catalog-education.oracle.com/pls/certview/sharebadge?id=1BBB15E94D645DE45156935112528F197168D2E99FF1C73FBB5D6779153A7E32"
    },
    "advanced course certification: machine learning & iot training": {
        "title": "Advanced Course Certification: Machine Learning & IoT Training",
        "organization": "SAP | Code Unnati",
        "details": "Participated in training on Machine Learning, IoT, Deep Learning, Computer Vision, and ABAP under the Code Unnati Program.",
        "date": "May 01, 2024",
        "link": "https://codeunnati.edunetfoundation.com/verify-certificate/CU24_8889"
    },
    "successfully completion of internship": {
        "title": "Successfully Completion of Internship",
        "organization": "Smartters Software",
        "details": "Successfully completed an internship at Smartters Software, where I gained valuable practical experience by contributing to real-world projects in software development and project management.",
        "date": "August 31, 2024",
        "link": "https://drive.google.com/file/d/1YiFImKXrM7FwNQ0L7i9YBWoLQHUwWwHX/view?usp=drive_link"
    },
    "advanace java": { # Note: This might be "Advanced Java" but using the key as provided in JS
        "title": "Advanace Java",
        "organization": "Royal Technosoft",
        "details": "Participated in an Advanced Java course, focusing on complex programming concepts and Java application development.",
        "date": "April 04, 2024",
        "link": "https://certopus.com/c/6f0242c3e46d42078ee4968f5ce8d5e4"
    }
}

EXPERIENCE_DATA = {
    "smartters": [
        {
            "title": "MERN Stack Developer",
            "date": "August 2024 - Present",
            "points": [
                "Developed and maintained real-time applications and RESTful APIs using Feathers.js within the MERN stack.",
                "Improved application performance by 20% through optimization and refactoring of existing code."
            ],
        },
        {
            "title": "MERN Stack Developer Intern",
            "date": "February 2024 - August 2024",
            "points": [
                "Developed and maintained real-time applications and RESTful APIs using Feathers.js within the MERN stack.",
                "Improved application performance by 20% through optimization and refactoring of existing code.",
                "Backend developer for 'Binimise,' a semi-government management portal used by municipal corporations to centralize fleet management, service notification, vendor tracking, complaints, and reporting. I focus on building and optimizing features like task management, complaint handling, report genera on, and custom field (EVA) functionality to enhance resource efficiency and operational effectiveness."
            ],
        },
    ]
    # Add other companies here if you have more experience later
}

class ActionListAllProjectLinks(Action): # NEW CUSTOM ACTION
    def name(self) -> Text:
        return "action_list_all_project_links"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_messages = ["Here are the live demo links for Sahil's projects:\n"]
        has_links = False
        for project_key, project_info in PROJECT_DATA.items():
            if project_info.get("host"):
                project_messages.append(f"- **{project_info['title']}**: {project_info['host']}")
                has_links = True

        if not has_links:
            dispatcher.utter_message(text="I don't have live demo links for any projects at the moment, but you can explore them on Sahil's projects page: https://sahilumraniya.vercel.app/projects")
        else:
            dispatcher.utter_message(text="\n".join(project_messages))

        return []

class ActionTellProjectDetails(Action):
    def name(self) -> Text:
        return "action_tell_project_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        project_name = tracker.get_slot("project_name")

        if project_name and project_name.lower() in PROJECT_DATA:
            project_info = PROJECT_DATA[project_name.lower()]
            message = (
                f"**{project_info['title']}**: {project_info['description']}\n"
                f"Technologies: {', '.join(project_info['tech'])}\n"
            )
            if project_info.get("github"):
                message += f"GitHub: {project_info['github']}\n"
            if project_info.get("host"):
                message += f"Live Demo/Host: {project_info['host']}"
        else:
            message = (
                f"I don't have detailed information for the project '{project_name if project_name else 'that'}'."
                " You can ask about projects like 'Swap & Share', 'AI Maze Solver', or 'Learnfinity'."
            )

        dispatcher.utter_message(text=message)
        return []

class ActionTellSkillDetails(Action):
    def name(self) -> Text:
        return "action_tell_skill_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        skill_name = tracker.get_slot("skill_name")

        if skill_name and skill_name.lower() in SKILL_DATA:
            message = SKILL_DATA[skill_name.lower()]
        else:
            message = (
                f"I don't have detailed information for the skill '{skill_name if skill_name else 'that'}'. "
                "You can ask about skills like Python, JavaScript, React JS, Node JS, MongoDB, or Docker."
            )

        dispatcher.utter_message(text=message)
        return []


class ActionTellAchievementDetails(Action): # NEW CUSTOM ACTION
    def name(self) -> Text:
        return "action_tell_achievement_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        achievement_title = tracker.get_slot("achievement_title")

        if achievement_title and achievement_title.lower() in ACHIEVEMENT_DATA:
            achievement_info = ACHIEVEMENT_DATA[achievement_title.lower()]
            message = (
                f"**{achievement_info['title']}** from {achievement_info['organization']} ({achievement_info['date']}): "
                f"{achievement_info['details']}\n"
            )
            if achievement_info.get("link"):
                message += f"Link: {achievement_info['link']}"
        else:
            message = (
                f"I don't have detailed information for the achievement '{achievement_title if achievement_title else 'that'}'. "
                "You can ask about 'Oracle Cloud Infrastructure Generative AI Certified Professional' or 'SAP Advanced Course Certification'."
            )

        dispatcher.utter_message(text=message)
        return []


class ActionTellExperienceByCompany(Action): # NEW CUSTOM ACTION
    def name(self) -> Text:
        return "action_tell_experience_by_company"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        company_name = tracker.get_slot("company_name")

        if company_name and company_name.lower() in EXPERIENCE_DATA:
            experiences_at_company = EXPERIENCE_DATA[company_name.lower()]
            messages = [f"Here's Sahil's experience at **{company_name.title()}**:\n"]
            for exp in experiences_at_company:
                points_list = "\n".join([f"  - {p}" for p in exp['points']])
                messages.append(
                    f"**{exp['title']}** ({exp['date']})\n"
                    f"{points_list}\n"
                )
            dispatcher.utter_message(text="\n".join(messages))
        else:
            dispatcher.utter_message(text="I don't have detailed experience for that company. Sahil's primary experience is with Smartters. Would you like to know about that?")
            # Optionally, you could set a slot to ask specifically about Smartters here
            # return [SlotSet("company_name", None)]

        return []