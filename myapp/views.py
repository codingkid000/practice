from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import collections.abc
collections.Hashable = collections.abc.Hashable




bot=ChatBot('chatbot',read_only=False,logic_adapters=[{
                                            'import_path':'chatterbot.logic.BestMatch',
                                            'default_response' : 'Sorry , I dont know what that means',
                                            #'maximum_similarity_threshold' :10
                                                      }])

list_to_train=[
    "hi",
    "hi there",
    "what's you'r name",
    "I am just a chatbot",
    "what is you'r fav food?",
    "I like cheese",
    "Who is created you",
    "I was created by Harilal",
    'who is the prime minister of india',
    'Shri Narendra Modi is the current and the fourth longest-serving Prime Minister of India. He served as the Chief Minister of Gujarat for 14 years and was applauded for the economic growth and setting up advanced infrastructure in the state, among other key developments.',
    'who is the chief minister of tamilnadu',
    'Honorable  Chief Minister of Tamil Nadu Thiru M.K.Stalin is the Head of the elected Government and heads the Council of Ministers.',
    "chief minister of tamil nadu",
    "Muthuvel Karunanidhi Stalin, often referred to by his initials as M. K. Stalin, is an Indian politician serving as the 8th and current Chief Minister of Tamil Nadu. The son of the former Chief Minister M. Karunanidhi, Stalin has been the president of the Dravida Munnetra Kazhagam party since 28 August 2018."
    "who is chief minister of tamil nadu"
    "Muthuvel Karunanidhi Stalin is the present CM of Tamilnadu. He took the oath as the 8th Chief Minister of Tamil Nadu on May 7, 2021, after the 2021 Tamil Nadu Legislative Assembly election."
]

#list_trainer=ListTrainer(bot)
#list_trainer.train(list_to_train)

chatterbotCorpusTrainer=ChatterBotCorpusTrainer(bot)
chatterbotCorpusTrainer.train("chatterbot.corpus.english")


def my_data(request):
    return render(request,"my_data.html")

def my_response(request):
    My_list=[1,2,3,4]
    return HttpResponse(My_list)


def getResponse(request):
    userMessage=request.GET.get('userMessage')
    chatResponce = str(bot.get_response(userMessage))
    print(chatResponce)
    return HttpResponse(chatResponce)


