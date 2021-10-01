'''AGE CALCULATOR BY RUDRA SANYAL IN a YEAR, b MONTH,c DAYS format'''

def get_age(day,month,yr,cd,cm,cy):
          a=0
          b=0
          c=0
          dlp={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:30,9:31,10:30,11:31,12:30}
          dnp={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:30,9:31,10:30,11:31,12:30}
          if cm<month:
               a=cy-yr-1
               if cd>day:
                 b=12-month+cm
                 c=cd-day
               else:
                 b=12-month+cm-1
                 if( yr%4==0):
                    if cm==1:
                       c=31-day+cd  
                    else:
                       c=dlp[cm-1]-day+cd
                 else:
                     if cm==1:
                       c=31-day+cd  
                     else:
                       c=dnp[cm-1]-day+cd
               return str(str(a)+" "+"year"+" "+str(b)+" "+"month"+" "+str(c)+" "+"days")
          elif cm==month:
              if(cy==yr):
                  a=0
                  b=0
                  c=cd-day
              else:
                  if(cd>=day):
                   a=cy-yr
                   b=0
                   c=cd-day
                  else:
                   a=cy-yr-1
                   b=11
                   if(yr%4==0):
                    if cm==1:
                       c=31-day+cd  
                    else:
                       c=dlp[cm-1]-day+cd
                   else:
                     if cm==1:
                       c=31-day+cd  
                     else:
                       c=dnp[cm-1]-day+cd
              return str(str(a)+" "+"year"+" "+str(b)+" "+"month"+" "+str(c)+" "+"days")
          else:
             a=cy-yr
             if cd>=day:
                 b=cm-month
                 c=cd-day
             else:
                b=cm-month-1
                if( yr%4==0):
                    c=dlp[month]-day+cd
                else:
                    c=dnp[month]-day+cd
                    
             return str(str(a)+" "+"year"+" "+str(b)+" "+"month"+" "+str(c)+" "+"days")
            
#input section
'''taking dob as input'''
day=int(input('enter day of dob'))
month=int(input('enter month of dob'))
yr=int(input('enter year of dob'))

'''taking  date at which we have to calcute dob'''
cd=int(input('enter current day'))
cm=int(input('enter current month'))
cy=int(input('enter current year'))

'''calling function to calculate age'''
print(get_age(day,month,yr,cd,cm,cy))
