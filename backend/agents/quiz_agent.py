import random


class QuizAgent:

    def __init__(self):

        self.current_quiz = []

        self.question_bank = {

            "HTML": [
                {"question": "What does HTML stand for?", "options": ["HyperText Markup Language", "High Transfer Machine Language", "Hyper Tool Multi Language", "Home Text Markup Language"], "answer": "HyperText Markup Language"},
                {"question": "Which tag is used for the largest heading?", "options": ["<h1>", "<h6>", "<heading>", "<head>"], "answer": "<h1>"},
                {"question": "Which HTML element is used for a hyperlink?", "options": ["<a>", "<link>", "<href>", "<nav>"], "answer": "<a>"},
                {"question": "What is the correct HTML element for inserting a line break?", "options": ["<br>", "<lb>", "<break>", "<newline>"], "answer": "<br>"},
                {"question": "Which tag is used to define an unordered list?", "options": ["<ul>", "<ol>", "<li>", "<list>"], "answer": "<ul>"}
            ],

            "CSS": [
                {"question": "What does CSS stand for?", "options": ["Cascading Style Sheets", "Computer Style Sheets", "Creative Style System", "Colorful Style Sheets"], "answer": "Cascading Style Sheets"},
                {"question": "Which property changes the text color?", "options": ["color", "text-color", "font-color", "foreground"], "answer": "color"},
                {"question": "Which CSS property controls text size?", "options": ["font-size", "text-size", "font-style", "text-style"], "answer": "font-size"},
                {"question": "How do you select an element with id 'demo'?", "options": ["#demo", ".demo", "demo", "*demo"], "answer": "#demo"},
                {"question": "Which property creates space inside an element?", "options": ["padding", "margin", "border", "spacing"], "answer": "padding"}
            ],

            "JavaScript": [
                {"question": "Inside which HTML element do we put JavaScript?", "options": ["<script>", "<js>", "<javascript>", "<code>"], "answer": "<script>"},
                {"question": "How do you create a function in JavaScript?", "options": ["function myFunc()", "create myFunc()", "def myFunc()", "func myFunc()"], "answer": "function myFunc()"},
                {"question": "How do you write an IF statement in JavaScript?", "options": ["if (i == 5)", "if i = 5 then", "if i == 5 then", "if (i = 5)"], "answer": "if (i == 5)"},
                {"question": "Which operator is used for strict equality?", "options": ["===", "==", "!=", "="], "answer": "==="},
                {"question": "Which method converts JSON to a JavaScript object?", "options": ["JSON.parse()", "JSON.stringify()", "JSON.convert()", "JSON.object()"], "answer": "JSON.parse()"}
            ],

            "React": [
                {"question": "React is developed by which company?", "options": ["Facebook (Meta)", "Google", "Amazon", "Microsoft"], "answer": "Facebook (Meta)"},
                {"question": "What is used to pass data between React components?", "options": ["Props", "DOM", "Render", "setState"], "answer": "Props"},
                {"question": "What hook is used for state management?", "options": ["useState", "useEffect", "useContext", "useRef"], "answer": "useState"},
                {"question": "JSX stands for?", "options": ["JavaScript XML", "Java Syntax Extension", "JSON XML", "JavaScript Extension"], "answer": "JavaScript XML"},
                {"question": "Which method renders React to the DOM?", "options": ["ReactDOM.render()", "React.render()", "DOM.render()", "render.React()"], "answer": "ReactDOM.render()"}
            ],

            "TypeScript": [
                {"question": "TypeScript is a superset of which language?", "options": ["JavaScript", "Java", "Python", "C++"], "answer": "JavaScript"},
                {"question": "Which keyword defines a type alias?", "options": ["type", "alias", "typedef", "define"], "answer": "type"},
                {"question": "What is the file extension for TypeScript?", "options": [".ts", ".typescript", ".tp", ".tsc"], "answer": ".ts"},
                {"question": "Which type allows any value?", "options": ["any", "void", "unknown", "all"], "answer": "any"},
                {"question": "How do you define an interface?", "options": ["interface MyInterface {}", "class MyInterface {}", "type MyInterface {}", "struct MyInterface {}"], "answer": "interface MyInterface {}"}
            ],

            "Java": [

                {
                    "question": "Which keyword is used to create an object in Java?",
                    "options": ["new", "this", "super", "class"],
                    "answer": "new"
                },

                {
                    "question": "Which loop executes at least once?",
                    "options": ["for", "while", "do while", "foreach"],
                    "answer": "do while"
                },

                {
                    "question": "Java is a ____ language.",
                    "options": [
                        "Object Oriented",
                        "Procedural",
                        "Assembly",
                        "Machine"
                    ],
                    "answer": "Object Oriented"
                },

                {
                    "question": "Which method is the entry point of a Java program?",
                    "options": [
                        "main()",
                        "start()",
                        "run()",
                        "execute()"
                    ],
                    "answer": "main()"
                },

                {
                    "question": "Which package is imported automatically?",
                    "options": [
                        "java.lang",
                        "java.util",
                        "java.io",
                        "java.sql"
                    ],
                    "answer": "java.lang"
                },

                {
                    "question": "Which keyword is used for inheritance?",
                    "options": [
                        "extends",
                        "implements",
                        "inherits",
                        "super"
                    ],
                    "answer": "extends"
                }

            ],

            "SQL": [

                {
                    "question": "Which SQL statement retrieves data?",
                    "options": [
                        "SELECT",
                        "INSERT",
                        "DELETE",
                        "UPDATE"
                    ],
                    "answer": "SELECT"
                },

                {
                    "question": "Which clause filters rows?",
                    "options": [
                        "WHERE",
                        "GROUP BY",
                        "ORDER BY",
                        "HAVING"
                    ],
                    "answer": "WHERE"
                },

                {
                    "question": "Which JOIN returns matching rows only?",
                    "options": [
                        "INNER JOIN",
                        "LEFT JOIN",
                        "RIGHT JOIN",
                        "FULL JOIN"
                    ],
                    "answer": "INNER JOIN"
                },

                {
                    "question": "COUNT() is an ______ function.",
                    "options": [
                        "Aggregate",
                        "Scalar",
                        "Date",
                        "String"
                    ],
                    "answer": "Aggregate"
                },

                {
                    "question": "Primary Key can contain NULL values.",
                    "options": [
                        "True",
                        "False"
                    ],
                    "answer": "False"
                }

            ],

            "Spring Boot": [

                {
                    "question": "Spring Boot is built on top of?",
                    "options": [
                        "Spring Framework",
                        "Hibernate",
                        "Servlet",
                        "JPA"
                    ],
                    "answer": "Spring Framework"
                },

                {
                    "question": "@RestController is used to create?",
                    "options": [
                        "REST APIs",
                        "Database",
                        "Frontend",
                        "Security"
                    ],
                    "answer": "REST APIs"
                },

                {
                    "question": "Which file stores Spring configuration?",
                    "options": [
                        "application.properties",
                        "config.java",
                        "pom.xml",
                        "index.html"
                    ],
                    "answer": "application.properties"
                },

                {
                    "question": "Spring Boot default embedded server is?",
                    "options": [
                        "Tomcat",
                        "Glassfish",
                        "JBoss",
                        "Jetty"
                    ],
                    "answer": "Tomcat"
                }

            ]

        }

    def generate_quiz(self, data):

        topic = data.topic.strip()

        if topic not in self.question_bank:
            # Generate generic fallback quiz
            questions = [
                {
                    "question": f"What is the primary purpose of {topic}?",
                    "options": [f"To build {topic} applications", "To style web pages", "To manage databases", "To query servers"],
                    "answer": f"To build {topic} applications"
                },
                {
                    "question": f"Which of the following best describes {topic}?",
                    "options": ["A framework", "A programming language", "A library", "Depends on the context"],
                    "answer": "Depends on the context"
                },
                {
                    "question": f"Is {topic} widely used in the industry?",
                    "options": ["Yes, it is very popular", "No, it is obsolete", "Only for personal projects", "Rarely used"],
                    "answer": "Yes, it is very popular"
                },
                {
                    "question": f"What is a common tool used with {topic}?",
                    "options": ["VS Code", "Hammer", "Wrench", "Oven"],
                    "answer": "VS Code"
                },
                {
                    "question": f"How do you deploy a {topic} project?",
                    "options": ["Using a cloud provider like AWS or Vercel", "By printing it out", "By saving it on a floppy disk", "You cannot deploy it"],
                    "answer": "Using a cloud provider like AWS or Vercel"
                }
            ]
        else:
            questions = self.question_bank[topic][:]

        random.shuffle(questions)

        selected = questions[:data.num_questions]

        quiz = []

        for index, q in enumerate(selected, start=1):

            options = q["options"][:]
            random.shuffle(options)

            quiz.append({

                "id": index,
                "question": q["question"],
                "options": options,
                "answer": q["answer"]

            })

        # Store quiz internally for Evaluation Agent
        self.current_quiz = quiz

        # Return questions WITHOUT answers
        return {

            "topic": topic,

            "difficulty": data.difficulty,

            "total_questions": len(quiz),

            "questions": [

                {
                    "id": q["id"],
                    "question": q["question"],
                    "options": q["options"]
                }

                for q in quiz

            ]

        }


quiz_agent = QuizAgent()