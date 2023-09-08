from django.shortcuts import render

def home(request):
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
    authors = [
        {
            'author': '🐼Hà Tường Nguyên',
            'job': '💻Computer Science',
            'position': 'OEC\'s Logistics',
            'content': Nguyen_content,
            'fb': 'https://www.facebook.com/HaTuongNguyenkute',
            'github': 'https://github.com/nguyenpanda',
        },
        {
            'author': '🥴Võ Trương Minh Ánh',
            'job': '💊Chemical Engineering',
            'position': 'OEC\'s Academic',
            'content': Anh_content,
            'fb': 'https://www.facebook.com/profile.php?id=100009112758992',
            'github': 'https://github.com/bad-chemist-is-coding',
        }
    ]
    context = {
        'authors': authors
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def TheStoriesOfOEC_1(request):
    contentEng = """\
Hello little German fans who are in a cave in the middle of a lonely World Cup winter 😣😣
—------------------------
If I go out now, wearing a Japanese navy blue shirt, I think it's like the king is wearing a long robe. As for 𝗢𝗜𝗦𝗣 𝗘𝗻𝗴𝗹𝗶𝘀𝗵 𝗖𝗹𝘂𝗯 (𝗢𝗘𝗖), wearing a blue shirt is a feeling of relief, joy and dynamism 🥸🥸
In 𝗢𝗘𝗖, it's not just about speaking English guys. There are 2 strangers, a boy and a girl, walking aimlessly together in our university and then suddenly encountering two very talented members of 𝗢𝗘𝗖 before asking them some questions. Please watch until the end of the clip for more details 👀👀
Perhaps the power of friendship is what makes the miracles happen during this special World Cup taking place in Qatar, and that must be true for the 𝗢𝗘𝗖 as well. The whole family of HCMUT are studying hard to prepare for the final exam, right? Yah, of course, me too so we would like to bring a joyful atmosphere that dispels all stress and worries for everyone 😇😇
Hope you will accompany 𝗢𝗘𝗖 in upcoming activities and projects. Now, the guys who passed the interview round of our club are practicing day and night to become official members. We will definitely recruit more members in the future. Let’s see 😉😉
Last but not least, don't forget to study well for the final exam to win a scholarship to show off to your parents, friends and lovers 🤟🤟
"""
    contentVie = """\
Hello mấy bạn fan Đức bé nhỏ đang ở trong hang giữa mùa đông World Cup cô đơn 😣😣
—---------------------------
Nếu bây giờ ra đường, khoác lên mình chiếc áo xanh biển của người Nhật, tôi cứ ngỡ như là vua đang mặc long bào vậy. Còn đối với OISP English Club (OEC), mặc chiếc áo xanh da trời lên là thấy bay bổng, nhẹ nhàng, vui tươi và năng động rồi đó 🥸🥸
Vào OEC đâu chỉ có mỗi nói tiếng Anh thôi đâu mọi người. Có hai bạn trai xinh, gái đẹp đi vu vơ trong trường rồi tự nhiên bắt gặp, rồi tự nhiên phỏng vấn hai bạn quá trời tài năng của 𝗢𝗘𝗖 nè. Mọi người coi đến hết clip để biết thêm chi tiết ha 👀👀 
Có lẽ sức mạnh của tình bạn là điều làm nên những kỳ tích trong kỳ World Cup đặc biệt đang diễn ra trên đất Qatar và điều đó chắc cũng đúng với 𝗢𝗘𝗖 nữa đó. Cả nhà yêu BKHCM  đang ráo riết ôn tập để chuẩn bị thi cuối kỳ đồ nè phải hong? Tụi mình muốn đem đến không khí vui tươi xua tan mọi căng thẳng, lo âu đồ cho mọi người nè 😇😇
Hi vọng bạn sẽ đồng hành cùng 𝗢𝗘𝗖 chúng mình trong những hoạt động và dự án sắp tới he. Giờ thì mấy bạn đậu vòng phỏng vấn của CLB mình đang luyện tập ráo riết để thành thành viên chính thức á. Tương lai chắc tụi mình sẽ tuyển quân nữa á. Mọi người cùng chờ xem 😉😉
Và cũng đừng quên ôn thi cuối kì thiệt tốt để rinh học bổng về khoe ba mẹ, bạn bè, người yêu he 🤟🤟
"""
    context = {
        'contentVie': contentVie,
        'contentEng': contentEng,
        'title': 'The Stories Of OEC I',
        'subtitle': '[𝗧𝗛𝗘 𝗦𝗧𝗢𝗥𝗜𝗘𝗦 𝗢𝗙 𝗢𝗘𝗖]',
        'link': 'https://fb.watch/mVWmE3CpQ1/',
        'video': 'https://www.facebook.com/plugins/video.php?height=314&href=https%3A%2F%2Fwww.facebook.com%2Foispenglishclub%2Fvideos%2F1158574251746368%2F&show_text=false&width=560&t=0'
    }
    return render(request, 'blog/story_base.html', context)

def TheStoriesOfOEC_2(request):
    contentEng = """\
🎶"Mừng Tết đến và lộc đến nhà nhà"🎶. Oh, wait! Before going home to celebrate Tet, let's stay with 𝗢𝗜𝗦𝗣 𝗘𝗡𝗚𝗟𝗜𝗦𝗛 𝗖𝗟𝗨𝗕 (𝗢𝗘𝗖) to "wait" for the “𝗧𝗛𝗘 𝗦𝗧𝗢𝗥𝗬 𝗢𝗙 𝗢𝗘𝗖" series🥳
Coming to this episode, you will be surprised by the appearance of OEC "𝘥𝘦𝘢𝘥𝘭𝘪𝘯𝘦 𝘸𝘢𝘳𝘳𝘪𝘰𝘳𝘴"😤
🌟If Tet is about having Banh Chung, Banh Tet, lucky money🧧 and many other things, then with our "deadline warriors what will they need to be able to "weigh" all the tasks assigned by OEC out🤔 Dear all, our HCMUT's guys, what are you waiting for to watch right now🔥 
Hopefully, through this video, it will help you love OEC even more. And, please keep waiting for our upcoming programs and events 😘
"""
    contentVie = """\
🎶“Mừng Tết đến và lộc đến nhà nhà”🎶. À mà khoan! Trước khi về quê ăn Tết, hãy cùng nán lại với 𝗢𝗜𝗦𝗣 𝗘𝗡𝗚𝗟𝗜𝗦𝗛 𝗖𝗟𝗨𝗕 (𝗢𝗘𝗖) để “hóng” tiếp diễn biến của “𝗖𝗵𝘂𝘆𝗲̣̂𝗻 𝗻𝗵𝗮̀ 𝗢̂ 𝗘 𝗖𝗲̂”🥳
Đến với tập lần này, cậu sẽ không khỏi ngạc nhiên với sự xuất hiện của những “𝘤𝘩𝘪𝘦̂́𝘯 𝘵𝘩𝘢̂̀𝘯 𝘥𝘦𝘢𝘥𝘭𝘪𝘯𝘦" OEC😤
🌟Nếu Tết là phải có bánh chưng, bánh tét, phong bao lì xì🧧 và nhiều thứ khác, vậy thì với những “chiến thần deadline của chúng ta họ sẽ cần gì để có thể “cân” hết mọi nhiệm vụ mà OEC giao ra 🤔 Hỡi cả nhà thân yêu BKHCM của chúng ta, còn chần chừ gì mà không xem “ngay và luôn” nào🔥
Hy vọng, thông qua video này, giúp các bạn thêm yêu OEC chúng mình hơn nữa 🤩và hãy cùng chúng mình đón chờ những chương trình, sự kiện sắp tới nhé😘
"""
    context = {
        'contentVie': contentVie,
        'contentEng': contentEng,
        'title': 'The Stories Of OEC II',
        'subtitle': '[𝗧𝗛𝗘 𝗦𝗧𝗢𝗥𝗜𝗘𝗦 𝗢𝗙 𝗢𝗘𝗖] - 𝗣𝗔𝗥𝗧 𝟮',
        'link': 'https://fb.watch/mVVG5i9LXD/',
        'video': 'https://www.facebook.com/plugins/video.php?height=314&href=https%3A%2F%2Fwww.facebook.com%2Foispenglishclub%2Fvideos%2F3294505030801189%2F&show_text=false&width=560&t=0'
    }
    return render(request, 'blog/story_base.html', context)

# def hello(request):
#     return render(request, 'blog/hello.html')
