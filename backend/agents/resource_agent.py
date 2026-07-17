class ResourceAgent:

    def __init__(self):

        self.resources = {

            "HTML": {
                "videos": [
                    {"title": "HTML Full Course - freeCodeCamp", "url": "https://www.youtube.com/results?search_query=html+full+course+freecodecamp"},
                    {"title": "HTML Crash Course - Traversy Media", "url": "https://www.youtube.com/results?search_query=html+crash+course+traversy+media"}
                ],
                "articles": [
                    {"title": "MDN HTML Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/HTML"},
                    {"title": "W3Schools HTML", "url": "https://www.w3schools.com/html/"}
                ],
                "practice": [
                    {"platform": "freeCodeCamp", "problem": "Responsive Web Design - HTML"},
                    {"platform": "HackerRank", "problem": "HTML/CSS Challenges"}
                ],
                "mini_project": "Personal Portfolio Page",
                "estimated_time": "2 Hours"
            },

            "CSS": {
                "videos": [
                    {"title": "CSS Full Course - freeCodeCamp", "url": "https://www.youtube.com/results?search_query=css+full+course+freecodecamp"},
                    {"title": "CSS Flexbox & Grid - Kevin Powell", "url": "https://www.youtube.com/results?search_query=css+flexbox+grid+kevin+powell"}
                ],
                "articles": [
                    {"title": "MDN CSS Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/CSS"},
                    {"title": "CSS-Tricks", "url": "https://css-tricks.com/"}
                ],
                "practice": [
                    {"platform": "Frontend Mentor", "problem": "Responsive Card Component"},
                    {"platform": "Flexbox Froggy", "problem": "CSS Flexbox Game"}
                ],
                "mini_project": "Responsive Landing Page",
                "estimated_time": "3 Hours"
            },

            "JavaScript": {
                "videos": [
                    {"title": "JavaScript Full Course - Bro Code", "url": "https://www.youtube.com/results?search_query=javascript+full+course+bro+code"},
                    {"title": "JS Crash Course - Traversy Media", "url": "https://www.youtube.com/results?search_query=javascript+crash+course+traversy+media"}
                ],
                "articles": [
                    {"title": "MDN JavaScript Guide", "url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide"},
                    {"title": "JavaScript.info", "url": "https://javascript.info/"}
                ],
                "practice": [
                    {"platform": "LeetCode", "problem": "Two Sum"},
                    {"platform": "HackerRank", "problem": "10 Days of JavaScript"}
                ],
                "mini_project": "Interactive To-Do App",
                "estimated_time": "3 Hours"
            },

            "React": {
                "videos": [
                    {"title": "React Full Course - freeCodeCamp", "url": "https://www.youtube.com/results?search_query=react+full+course+freecodecamp"},
                    {"title": "React Tutorial - Codevolution", "url": "https://www.youtube.com/results?search_query=react+tutorial+codevolution"}
                ],
                "articles": [
                    {"title": "React Official Docs", "url": "https://react.dev/"},
                    {"title": "React Tutorial - W3Schools", "url": "https://www.w3schools.com/react/"}
                ],
                "practice": [
                    {"platform": "Build", "problem": "Weather App using React"},
                    {"platform": "Build", "problem": "Todo List with State Management"}
                ],
                "mini_project": "Movie Search App with React",
                "estimated_time": "4 Hours"
            },

            "TypeScript": {
                "videos": [
                    {"title": "TypeScript Full Course", "url": "https://www.youtube.com/results?search_query=typescript+full+course"},
                    {"title": "TypeScript for Beginners", "url": "https://www.youtube.com/results?search_query=typescript+beginners+tutorial"}
                ],
                "articles": [
                    {"title": "TypeScript Official Handbook", "url": "https://www.typescriptlang.org/docs/handbook/"},
                    {"title": "TypeScript Deep Dive", "url": "https://basarat.gitbook.io/typescript/"}
                ],
                "practice": [
                    {"platform": "TypeScript Exercises", "problem": "Type Challenges"},
                    {"platform": "Build", "problem": "Typed API Client"}
                ],
                "mini_project": "Type-safe REST API Client",
                "estimated_time": "3 Hours"
            },

            "Java": {

                "videos": [
                    {
                        "title": "Java Full Course - Bro Code",
                        "url": "https://www.youtube.com/results?search_query=java+bro+code"
                    },
                    {
                        "title": "Java Placement Course - Apna College",
                        "url": "https://www.youtube.com/results?search_query=java+apna+college"
                    }
                ],

                "articles": [
                    {
                        "title": "Oracle Java Documentation",
                        "url": "https://docs.oracle.com/javase/tutorial/"
                    },
                    {
                        "title": "W3Schools Java",
                        "url": "https://www.w3schools.com/java/"
                    }
                ],

                "practice": [
                    {
                        "platform": "LeetCode",
                        "problem": "Palindrome Number"
                    },
                    {
                        "platform": "LeetCode",
                        "problem": "Two Sum"
                    },
                    {
                        "platform": "HackerRank",
                        "problem": "Java Loops"
                    }
                ],

                "mini_project": "Student Management System",

                "estimated_time": "3 Hours"

            },

            "Spring Boot": {

                "videos": [
                    {
                        "title": "Spring Boot Tutorial",
                        "url": "https://www.youtube.com/results?search_query=spring+boot+course"
                    }
                ],

                "articles": [
                    {
                        "title": "Spring Official Documentation",
                        "url": "https://spring.io/guides"
                    }
                ],

                "practice": [
                    {
                        "platform": "Build",
                        "problem": "REST API CRUD Application"
                    }
                ],

                "mini_project": "Employee Management API",

                "estimated_time": "4 Hours"

            },

            "SQL": {

                "videos": [
                    {
                        "title": "SQL Full Course",
                        "url": "https://www.youtube.com/results?search_query=sql+course"
                    }
                ],

                "articles": [
                    {
                        "title": "SQLBolt",
                        "url": "https://sqlbolt.com/"
                    }
                ],

                "practice": [
                    {
                        "platform": "LeetCode",
                        "problem": "Combine Two Tables"
                    },
                    {
                        "platform": "LeetCode",
                        "problem": "Second Highest Salary"
                    }
                ],

                "mini_project": "Library Database",

                "estimated_time": "2.5 Hours"

            }

        }

    def get_resources(self, data):

        topic = data.topic

        if topic in self.resources:
            return {
                "topic": topic,
                "skill_level": data.skill_level,
                "learning_style": data.learning_style,
                **self.resources[topic]
            }

        # Dynamic Generic Fallback for ANY topic
        formatted_topic = topic.replace(" ", "+")
        return {
            "topic": topic,
            "skill_level": data.skill_level,
            "learning_style": data.learning_style,
            "videos": [
                {
                    "title": f"{topic} Full Course - Complete Tutorial",
                    "url": f"https://www.youtube.com/results?search_query={formatted_topic}+full+course"
                },
                {
                    "title": f"Learn {topic} in 1 Hour",
                    "url": f"https://www.youtube.com/results?search_query={formatted_topic}+in+1+hour"
                }
            ],
            "articles": [
                {
                    "title": f"Official {topic} Documentation",
                    "url": f"https://www.google.com/search?q={formatted_topic}+official+documentation"
                },
                {
                    "title": f"Getting Started with {topic}",
                    "url": f"https://www.google.com/search?q=Getting+Started+with+{formatted_topic}"
                }
            ],
            "practice": [
                {
                    "platform": "Practice Platform",
                    "problem": f"Basic {topic} Exercises"
                }
            ],
            "mini_project": f"Build a simple {topic} application",
            "estimated_time": "3 Hours"
        }


resource_agent = ResourceAgent()