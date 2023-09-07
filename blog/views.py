from django.shortcuts import render

Nguyen_content = """Hello there, \
I'm Ha Tuong Nguyen, currently a sophomore majoring in Computer Science at HCMUT. \
I'm a member of OISP English Club, specifically in the Logistics team. 

In the past, I've taken on roles as a monitor for the OEC booth at the OISP International Festival 2023, \
as well as a monitor for the Musical Weekly event, and served as the vice monitor for OEC End of Year Bonding in 2023. \
Furthermore, I've actively participated in various other OEC activities such as the Debate Battle 2023, OISP Club Day, \
and OISP Orientation Week. Throughout my time with OEC, I've not only acquired new knowledge but also had the \
privilege of meeting some incredibly remarkable individuals who have encouraged me to step beyond my comfort zone.
"""

Anh_content = """Hi, I am Vo Truong Minh Ánh from the Chemical Engineering faculty of HCM-UT. \
I am a second-year student with a 1 year experience in OISP English Club as an Academic team. \
With my passions and abilities, I used to be the monitor of OISP International Festival 2023 and other events, \
especially IELTS Buddy 2023 at the present. 

Even though taking part in events of club is a big challenge for those who usually participate in many competitions \
and aiming to achieve higher academic results like me, being a part of OEC was my great decision when I have chance \
to train my time management skills and other soft skills, as well as many other great characteristics like confidence \
(which support me in gaining high prizes in competition I joined) or team-work (which allowed me to work properly \
to get high results in studying). The greatest thing is that I met new wonderful friends  and other \
great relationships. I have no regrets at all.
"""

posts = [
    {
        'author': '🐼Hà Tường Nguyên',
        'job': '💻Computer Science - OEC\'s Logistics',
        'content': Nguyen_content,
    },
    {
        'author': '🥴Võ Trương Minh Ánh',
        'job': '💊Chemical Engineering - OEC\'s Academic',
        'content': Anh_content,
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def hello(request):
    return render(request, 'blog/hello.html')
