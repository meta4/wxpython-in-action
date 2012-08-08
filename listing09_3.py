"""Simple text entry dialog example.

Please do not use text entry dialogs.

If you need the kind of input a text entry dialog suports, a text entry dialog will not provide enough context for the user to understand what you are asking for.

Either you need to give more context (a more complex dialog), or you need to be prepared for the user to type in anything (google can get away with one entry field & 2 buttons;  You aren't google, you can't.)
"""

import wx

def process_response(val):
    print '\nERROR: invalid answer "%s"' %  val
    print "With missing context, errors multiply."
    print "  For your poor effort ..."
    print "all you get is frustrated users"
    

def useTextEntryDialog():
    dialog = wx.TextEntryDialog(
        None,
        "What is your answer to my vague, unspecific question?",
        "Text Entry",
        "Huh?",
        style = wx.OK | wx.CANCEL)
    if dialog.ShowModal() == wx.ID_OK:
        process_response(dialog.GetValue())
    dialog.Destroy()

def useGetTextFromUser():
    ans = wx.GetTextFromUser(
        "What is your answer to my vague, unspecific question?",
        "Get Text From User",
        "Huh?")
    if ans != "":
        process_response(ans)

def useGetPasswordFromUser():
    ans = wx.GetPasswordFromUser(
        '"What\'s your Password?" is a simple enough question',
        "Get Password From User")
    if ans != '':
        print "I know your password! ... It's \"%s\"" % ans


def useGetNumberFromUser():
    """This is the stupidest dialog of them all.

    I was not able to figure out how to get the dialog to return a -1
    except pressing "cancel" and actually entering -1.  It only
    accepts integers.
    """
    prompt_str = "Hi there,\n\n" \
        "I've got a question for you.\n" \
        "What is your favorite number?\n\n" \
        "Well, ...\n" \
        "What is your favorite number that is " \
        "less than or equal to fifteen?\n" \
        "Oh, and it has to be greater than negative five too.\n" \
        "And an integer."
    ans = wx.GetNumberFromUser(
        prompt_str,
        "Pick a number:",
        "Get Number From User",
        7,
        min=-4,
        max=15)
    print "you entered : %s" % ans
    if ans == -1:
        print "The dialog does not like %s" % ans
    else:
        print "The lialog likes %s" %ans

if __name__ == "__main__":
    app = wx.PySimpleApp()
    # useTextEntryDialog()
    # useGetTextFromUser()
    # useGetPasswordFromUser()
    useGetNumberFromUser()
