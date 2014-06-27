from util import hook
import random

@hook.command('debugwelcome')
@hook.event("JOIN")
def welcome(inp, chan=None, nick=None):
        if chan == "#eisenstein":
                value = random.randint(0, 8)
                valuestring = str(value)
                dict = {'0': 'I\'m not really alive, by the way.'};
                dict['1'] = "How are you today?";
                dict['2'] = "I hope you feel well.";
                dict['3'] = "It is good to see you back!";
                dict['4'] = "Making some coffee for you!";
                dict['5'] = "Really, welcome back!";
                dict['6'] = "Umm, Chocolate or Vanilla?";
                dict['7'] = "We missed you!";
                dict['8'] = "Here, have a sandwich!";
                comment = dict.get(valuestring, "Something went wrong");
                return "Welcome back " + nick + "!" + " " + comment
        else:
                response = "This is not the right channel"
