
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import gspread
from datetime import date
from dateutil import parser
import time

 




today = date.today()



TOKEN: Final = 'TOKEN BY TELEGRAM'
BOT_USERNAME: Final ='@Grama_2023_Bot'
sa = gspread.service_account(filename="JASON FILE BY GOOGLE DEV")
sh = sa.open("GramaLens_Money")
wks = sh.worksheet("Totals")



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a GramaBot. What\'s up?')


# Lets us use the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Welcome to GramaBot help panel i'm gonna show you what you can do with:
*Here is some basic commands*
/start - Starts the bot
/help - Shows you this message 
/profit - Shows you the total profits
/losses - Shows you the total losses
/rest - Shows you the total rest money
/worth - Shows you the total net worth

*Here is some basic messages*
profit - Show you the total profits
losses - Shows you the total losses
rest - Shows you the total rest money
version - to see the GramaBot version

*Here is some messages to control the bot*
stop - Stops any ongoing process

*Here is some controls for GramaLens Money*
add profit - lets you add a new profit to the database
delete profit - lets you delete lst profit in the database
add loss - lets you add a new loss to the database
delete loss - lets you delete lst loss in the database""",parse_mode= 'markdown')


# Lets us use the /profit command
async def profit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('GramaLens Total Profits: '+wks.acell('D5').value)

async def losses(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('GramaLens Total Losses: '+wks.acell('D6').value)

async def rest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('GramaLens Total Rest: '+wks.acell('D7').value)

async def worth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('GramaLens Total Worth: '+wks.acell('I5').value)





pr = 0
ls = 0
tarikh=client=des=prix = 0
start_time = current_time = elapsed_time = 0
redo_time_limit = 5*100
def handle_response(text: str) -> str:
   global user
   global pr
   global ls
   global tarikh,client,des,prix
   global start_time,current_time,elapsed_time,redo_time_limit

   processed: str = text.lower()
   if 'hello' in processed:
      return 'Hey there!'
   
   if 'how are you' in processed:
      return 'I am good!'
   
   if 'who is mohcine' in processed:
      return 'GramaLens Photographer 📸'
   if 'who is hanan bouzaga' in processed:
      return 'GramaLens Managment 📌'
   if 'who is hassan' in processed:
      return 'GramaLens lighting professional and clients finder 💡'
   if 'who is hanane sghir' in processed:
      return 'GramaLens accountant 💰'
   if 'who is badr' in processed:
      return 'GramaLens Videographer 🎦'
   if 'who is hanan' == processed or 'who is hanane' == processed:
      return 'which one do you mean [Hanane sghir or Hanan Bouzaga]'
   if 'من هو محسن' in processed or 'شكون محسن' in processed:
      return 'مصور فوتوغرافي في GramaLens 📸'
   if 'من هو بدر' in processed or 'شكون بدر' in processed:
      return 'مصور سينمائي في GramaLens 🎦'
   if 'من هو حسن' in processed or 'شكون حسن' in processed:
      return 'مختص في تجهيز الاضاءه وايجاد الزبائن في GramaLens 💡'
   if 'من هي حنان' == processed or 'شكون حنان' in processed:
      return 'ايهما تقصد [حنان سغير او حنان بوزاكة] ؟'
   if 'من هي حنان سغير' in processed or 'شكون حنان سغير' in processed:
      return 'محاسبة GramaLens 💰'
   if 'من هي حنان بوزاكا' in processed or 'شكون حنان بوزاكا' in processed:
      return 'مديرة مواعيد GramaLens 📌'
   if 'chkon bak' in processed or 'شكون باك' in processed:
      return 'Badr Karrachai 😎'
   if 'version' in processed or 'الاصدار' in processed:
      return '🤖 GramaBot 1.0.5'
   if 'شكون باك' in processed:
      return 'بدر كراشاي 😎'
   if 'الارباح' in processed or 'ربح' == processed or 'ماهي الارباح' in processed or 'profit' == processed:
      return 'GramaLens Total Profits: '+wks.acell('D5').value
   if 'الخسائر' in processed or 'خسائر' == processed or 'ماهي الخسائر' in processed or 'losses' == processed :
      return 'GramaLens Total Profits: '+wks.acell('D6').value
   if 'الباقي' in processed or 'باقي' == processed or 'ماهو الباقي' in processed or 'rest' == processed:
      return 'GramaLens Total Profits: '+wks.acell('D7').value  
# Add Profit
   if pr !=0:
      if 'stop' == processed or 'توقف' == processed or 'قف' == processed or 'stp' == processed:
         pr = 0
         tarikh=client=des=prix = 0
         return 'حسنا تم التراجع عن الاضافة 😒.'
      else:
         if pr == 1:
            try:
               user_date = parser.parse(processed, fuzzy=True)
               final_date = str(user_date)[:10]
            except:
               return """انا اسف ولكن هذا ليس تاريخا صحيحا! 
- ارسل تاريخا صحيحا او يمكن التراجع عن الادخال ب 'توقف' او 'stop'"""
            # open txt file
            with open('number_pr.txt') as f:
               line = f.read()

            tarikh = str(final_date)
            pr = pr+1
            return 'ما هو اسم الزبون؟'

         if pr == 2:
            # open txt file
            with open('number_pr.txt') as f:
               line = f.read()

            client = processed
            pr = pr+1
            return 'ما هو تعليقك؟'
         
         if pr == 3:
            # open txt file
            with open('number_pr.txt') as f:
               line = f.read()

            des = processed
            pr = pr+1
            return 'ما هو اجمالي الربح؟'
         
         if pr == 4:
            x=0
            try:
               x = int(processed)
            except:
               return """انا اسف ولكن هذا ليس ثمنا صحيحا! 
- ارسل ثمنا صحيحا او يمكن التراجع عن الادخال ب 'توقف' او 'stop'"""
            # open txt file
            with open('number_pr.txt') as f:
               line = f.read()
            
            prix = x

            # add to google sheets
            wks2 = sh.worksheet("Profits")
            wks2.update('A'+line,tarikh)
            wks2.update('B'+line,client)
            wks2.update('C'+line,des)
            wks2.update('D'+line,int(prix))
            tarikh=client=des=prix = 0

            pr = 0
            with open('number_pr.txt', 'w') as f:
               f.write(str(int(line)+1))
            # starts the redo timer
            redo_time_limit = 5 * 60
            start_time = time.time()
            return """تم حذف اخر تسجيل بنجاح ✅
( بعد خمس دقائق لن تتمكن من التراجع عن هذه العملية)"""

   if 'اضف ربح' == processed or 'add profit' == processed or 'ربح جديد' == processed or 'new profit' == processed or 'ajouter profit' == processed or 'new pr' == processed or 'ajouter pr' == processed or 'add pr' == processed:
      pr = pr+1
      return 'ما هو تاريخ هذا الاجراء؟'
# delete last profit
   if 'احذف ربح' == processed or 'delete profit' == processed or 'امسح ربح' == processed or 'delete the profit' == processed or 'delet the profit' == processed or 'delet profit' == processed or 'redo pr' == processed or 'del pr' == processed or 'Supprimer profit' == processed or 'delete pr' == processed or 'Supprimer pr' == processed:
      current_time = time.time()
      elapsed_time = current_time - start_time
      if elapsed_time <= redo_time_limit:
         with open('number_pr.txt') as f:
            x = int(f.read())-1
         line = str(x)
         wks2 = sh.worksheet("Profits")
         wks2.update('A'+line,'')
         wks2.update('B'+line,'')
         wks2.update('C'+line,'')
         wks2.update('D'+line,'')
         with open('number_pr.txt', 'w') as f:
            f.write(line)
         start_time = current_time = elapsed_time = 0
         redo_time_limit = 5*100
         return 'تم حذف اخر تسجيل بنجاح ✅'
      else:
         return 'اسف لقد تجاوزت الوقت المسموح به لاجراء هذه العملية ⛔'
# Add Losses
   if ls !=0:
      if 'stop' == processed or 'توقف' == processed or 'قف' == processed or 'stp' == processed:
         ls = 0
         tarikh=client=des=prix = 0
         return 'حسنا تم التراجع عن الاضافة 😒.'
      else:
         if ls == 1:
            try:
               user_date = parser.parse(processed, fuzzy=True)
               final_date = str(user_date)[:10]
            except:
               return """انا اسف ولكن هذا ليس تاريخا صحيحا! 
- ارسل تاريخا صحيحا او يمكن التراجع عن الادخال ب 'توقف' او 'stop'"""
            # open txt file
            with open('number_loss.txt') as f:
               line = f.read()

            tarikh = str(final_date)
            ls = ls+1
            return 'ما هو سبب هذه الخسارة؟'

         if ls == 2:
            # open txt file
            with open('number_loss.txt') as f:
               line = f.read()

            client = processed
            ls = ls+1
            return 'ما هو تعليقك؟'
         
         if ls == 3:
            # open txt file
            with open('number_loss.txt') as f:
               line = f.read()

            des = processed
            ls = ls+1
            return 'ما هو اجمالي الخسارة؟'
         
         if ls == 4:
            x=0
            try:
               x = int(processed)
            except:
               return """انا اسف ولكن هذا ليس ثمنا صحيحا! 
- ارسل ثمنا صحيحا او يمكن التراجع عن الادخال ب 'توقف' او 'stop'"""
            # open txt file
            with open('number_loss.txt') as f:
               line = f.read()
            
            prix = x

            # add to google sheets
            wks2 = sh.worksheet("Losses")
            wks2.update('A'+line,tarikh)
            wks2.update('B'+line,client)
            wks2.update('C'+line,des)
            wks2.update('D'+line,int(prix))
            tarikh=client=des=prix = 0

            ls = 0
            with open('number_loss.txt', 'w') as f:
               f.write(str(int(line)+1))
            # starts the redo timer
            redo_time_limit = 5 * 60
            start_time = time.time()
            return """تم حذف اخر تسجيل بنجاح ✅
( بعد خمس دقائق لن تتمكن من التراجع عن هذه العملية)"""

   if 'اضف خسارة' == processed or 'add loss' == processed or 'add los' == processed or 'add losses' == processed or 'خسارة جديد' == processed or 'ajouter loss' == processed or 'new ls' == processed or 'ajouter ls' == processed or 'ajouter los' == processed or 'add ls' == processed:
      ls = ls+1
      return 'ما هو تاريخ هذا الاجراء؟'
   # delete last profit
   if 'احذف خسارة' == processed or 'delete loss' == processed or 'امسح خسارة' == processed or 'delete the loss' == processed or 'delet the loss' == processed or 'delet loss' == processed or 'delete ls' == processed or 'd ls' == processed or 'redo ls' == processed or 'Supprimer losses' == processed or 'Supprimer loss' == processed or 'Supprimer los' == processed or 'Supprimer ls' == processed:
      current_time = time.time()
      elapsed_time = current_time - start_time
      if elapsed_time <= redo_time_limit:
         with open('number_loss.txt') as f:
            x = int(f.read())-1
         line = str(x)
         wks2 = sh.worksheet("Losses")
         wks2.update('A'+line,'')
         wks2.update('B'+line,'')
         wks2.update('C'+line,'')
         wks2.update('D'+line,'')
         start_time = current_time = elapsed_time = 0
         redo_time_limit = 5*100
         with open('number_loss.txt', 'w') as f:
            f.write(line)
         return 'تم حذف اخر تسجيل بنجاح ✅'
      else:
         return 'اسف لقد تجاوزت الوقت المسموح به لاجراء هذه العملية ⛔'
      
   return ''

   

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global pr
    global ls

    # Get basic info of the incoming message
    message_type: str = update.message.chat.type
    text: str = update.message.text

    # Print a log for debugging
   #  print(f'User ({update.message.chat.username}) == {message_type}: "{text}"')


    # React to group messages only if users mention the bot directly
    
    response: str = handle_response(text)

    # Reply normal if the message is == private
    if response != '':
      await update.message.reply_text(response)
    


# # Log errors
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f'Update {update} caused error {context.error}')

# Run the program
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('profit', profit))
    app.add_handler(CommandHandler('losses', losses))
    app.add_handler(CommandHandler('rest', rest))
    app.add_handler(CommandHandler('worth', worth))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Log all errors
   #  app.add_error_handler(error)

    print('Polling...')
    # Run the bot
    app.run_polling(poll_interval=5)