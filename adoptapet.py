start = '''
Welcome to Adopt-a-Pet Center! Pick your character Cindy or TJ
'''

Cindy= '''
You're 20 years old living in Seattle and have recently gone through a dramatic breakup with your bf.
You have decided to turn a new leaf, get up and see what else the world has to offer you.
You still want comanionship and have decided to adopt a cat from the nearest shelter.

When you walk in an employee says," How can I help you?""
Do you get into what happened with your bf or continue with the adoption process.
Type 'explain' or 'adopt'
'''

TJ= '''
You're 8 years old and have been begging your parents for a pet.
You live close to a shelter and your parents allow you to explore inside.
Near the cat corner is a orange striped Tabby named Max.
They make eye contect and the connection is clear, he has fallen in love with the cute ball of fur.

An employee walks up and if he would like to play with it.
You earnestly agree and decide that he is the one for you and ypou must take him home.
Do you beg you parents or master up a plan to get him.
Type 'beg' or 'plan'
'''
explain='''
Well, life has just been kind of rough. I was in a lovely relationship with this guy for the longest time
but I found out that he wasn't as loyal as I thought. *sobs* And you know what?! He was cheating on my with my
ex best friend. I mean life just can't get any worse right now.
I've been longing for some companionship lately and I think a cat would be perfect. Would I be able to adopt a cat?

The employee looks taken aback and says, "I think you need some time to clear your head and myabe getting a cat is
not the best option right now. Maybe consider getting an animal in a few months."

'''
adopt='''
You tell him that you are interested in adopting a cat. The employee leads you to the cat corner and shows you the three cats
available for adoption at the moment. You take a look around and your eyes land on this graceful snow white being. A Persian kitty
by the name of Belle. You tell the employee that Belle is the one for you. The employee asks if you are ready
and have done your research about taking care of a cat.
Type 'yes' or 'no'
'''
yes='''
You tell her that you completed all prior research and have already purchased all necessary equipment in the car.
'''
no='''
You go through with the whole adoption process anyways and on your way home you leave the door open of the car. Once you come
back from putting something in the house, you notice that the cat is no longer there...
'''
happyending ='''
Yay! You adopted a cat successfully today and found a companion. We hope you and your cat have a good life together.
The end.
'''
badending='''

'''
beg='''
You call your parents and beg for Max. You are so persistent that you start crying and your mom rushes over to make sure you
are ok. When she arrives at Adopt-a-Pet, she sees how passionate you are about having a cat.
'''
plan='''
You know your parents won't agree no matter what but you know that Max and you have a relationship that cannot be broken.
Something must be done.
Type 'steal' or 'scheme'
'''
steal='''
You check to make sure that the coast is clear and then you sneak into the cat corner, swiftly pick up max and book it.
'''
scheme='''
You call up your cousin Randy and tell him you need him to pretend to be your dad. He says, "Say no more! I'll be there in 5."
Randy walks into Adopt-a-Pet wih a business suit on and a briefcase. He speaks to the employee in a deep voice and tells him that he is your father.
The employee believes him and you continue with the adoption process.
'''
gameover='''
Uh-Oh. I guess you won't be getting a cat today. Game Over.
'''
print (start)
done = False
while not done:
    user_input = input("type 'Cindy' or 'TJ':")
    if user_input ==" Cindy ":
        print(Cindy)
    if user_input== "explain":
            print(explain)
        elif user_input == "adopt":
            print(adopt)
        if user_input== "yes":
            print(yes)
        elif user_input== "no":
            print(no)
        done = True
    elif user_input== "TJ":
        print(TJ)
        done= True
    else:
        print("Please type 'TJ' or 'Cindy'");
