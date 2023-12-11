from rich import print
from rich.text import Text
from rich.panel import Panel


# def get_email_body(company_name):
#     # Create a Text object for the main message
#     message = Text()



#     # Introduction
#     message.append("Dear Hiring Team,\n\n")

#     # Main content
#     message.append(f"I am writing to express my keen interest in the Software Engineering Intern/FTE role at {company_name}. As a final-year IT undergraduate at IIIT Lucknow, I am eager to contribute my skills and knowledge to your esteemed organization. I am available to join [bold]immediately[/bold] and have a diverse background in both [bold]competitive programming[/bold] and [bold]web development[/bold]. Attached to this email is my resume for your reference.\n\n")

#     # A bit about me
#     message.append("A bit about me:\n", style="underline")

#     # Internship
#     message.append("Internship\n")
#     message.append("    • [bold]Full Stack Developer Intern | Vani.ai (stealth startup)[/bold]\n")
#     message.append("      - Worked on backend, designed restful APIs.\n")
#     message.append("      - Worked on the database, wrote optimized queries.\n\n")

#     # Freelancing
#     message.append("Freelancing\n")
#     message.append("    • [bold]Teaching Assistant | Scaler[/bold]\n")
#     message.append("      - Mentored more than 650+ students in DSA, OOPS, and programming.\n")
#     message.append("    • [bold]Subject Matter Expert | Chegg[/bold]\n")
#     message.append("      - Resolved queries related to computer science, web development, math, and reasoning.\n\n")

#     # Volunteering
#     message.append("Volunteering\n")
#     message.append("• [bold]Senior member[/bold] of competitive programming wing at Axios (Technical society of IIIT Lucknow).\n")
#     message.append("• [bold]Member[/bold] of competitive programming wing at Axios.\n\n")

#     # Open Source
#     message.append("Open Source\n")
#     message.append("    • [bold]Hacktoberfest[/bold]\n")
#     message.append("      - [bold]Maintainer[/bold] in Hacktoberfest 2023\n")
#     message.append("      - Contributed to more than [bold]14[/bold] repos in Hacktoberfest 2022 and 2021.\n")
#     message.append("    • [bold]Girl Script Summer of Code (GSSOC)[/bold]\n")
#     message.append("      - Participated and merged [bold]10 PRs[/bold] in GSSOC 2021\n\n")

#     # Competitive Coding
#     message.append("Competitive Coding\n")
#     message.append("    • [bold]ACM ICPC: ICPC Gwalior Pune Regionalist 2021\n[/bold]")
#     message.append("    • Rated as [bold]Expert[/bold] on Codeforces (max rating: 1725) and among the [bold]top 700[/bold] coders in INDIA\n")
#     message.append("    • Rated as [bold]5 stars[/bold] on CodeChef (max rating: 2122) and among the [bold]top 300[/bold] coders in INDIA\n")
#     message.append("    • Rated as [bold]Knight[/bold] on LeetCode (max rating: 2079) and among the [bold]top 1.78%[/bold] globally\n")
#     message.append("    • [bold]Google Kickstart[/bold]: Got global [bold]rank 489[/bold] out of 30k+ participants\n")
#     message.append("    • [bold]Meta Hacker Cup[/bold]: Got [bold]AIR 105[/bold] in round 2\n\n")

#     # Hackathons
#     message.append("Hackathons\n")
#     message.append("    • [bold]Semifinalist[/bold] in Hack-o-Fiesta (Hackathon organized by IIIT Lucknow)\n")
#     message.append("    • [bold]Top 2k[/bold] among 400k+ teams in Flipkart Grid 2023\n")
#     message.append("    • Participated in [bold]Walmart[/bold] Spark Athon\n\n")

#     # Skills
#     message.append("I have experience working with technologies and frameworks such as [bold]Node.js, Next.js, Express, React, HTML/CSS, Flask, Fast API, Web Sockets, Socket.io, Machine learning, REST APIs, Python, C/C++, Java, and JavaScript, Git/GitHub, MySQL, SQL[/bold]. I believe these skills will make me a valuable asset to your team. I am enthusiastic about the opportunity to contribute to your company's success and growth.\n\n")

#     # Resume link
#     message.append("You can find my resume") 
#     message.append("[here](https://drive.google.com/file/d/1QYbrqwegTtCUnjGmPIymWpDTbphBxd_j/view).\n\n", style="blue underline")

#     # Closing
#     message.append("I am looking forward to hearing from you.\n\n")
#     message.append("Thanks and Regards,\n\n")
#     message.append("Sincerely,\nAnkit Kumar\n", style="bold")
#     message.append("+919315531864\n")

#     # Print the formatted message
#     return message


def get_email_body(name):
   return f"""

<p>This is <strong>rich text</strong> content.</p>
<b>You can use HTML tags to format your email body.</b>

"""

