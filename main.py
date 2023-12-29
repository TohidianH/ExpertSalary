from UI_Salary import *
from SalaryEval import *
from PyQt6.QtGui import *
import sys

A11T1Text='ماده 11 تبصره ۱ (اصلاحی ۱۴۰۲/۰۸/۲۰)- در صورتی که ارزش موضوع کارشناسی ۵۰.۰۰۰ میلیارد ریال یا بالاتر باشد شورای عالی کارشناسان و مرکز حسب مورد با کسب نظر کانون و یا مرکز استان مربوط، از بین کارشناسان استان محل کارشناسی، نسبت به انتخاب اعضای هیات کارشناسی، میزان دستمزد و روش پرداخت آن اتخاذ تصمیم می‌نماید.'
A11N3Text='ماده 11 تبصره ۳ (اصلاحی ۱۴۰۲/۰۸/۲۰)- دستمزد بررسی اختلاف بین کارفرمایان، پیمانکاران، مهندسان مشاور و همچنین قراردادهای مربوط و دستمزد کنترل و تعیین صورت وضعیت برای کلیه رشته‌ها، بر مبنای مبلغ قرارداد طبق این ماده به اضافه صد درصد می‌باشد. در صورتی که قرارداد مربوط سالهای قبل باشد، بر اساس شاخص قیمت سالانه مبلغ آن به روزرسانی‌ می‌شود. چنانچه کارشناسی صرفاً مربوط به بخشی از قرارداد مانند تشخیص تخلف از مفاد قرارداد و یا رسیدگی به تأخیر در انجام قرارداد باشد، دستمزد طبق این ماده به اضافه پنجاه درصد می‌باشد.'
A11N4Text='ماده 11 تبصره ۴ (اصلاحی ۱۴۰۲/۰۸/۲۰)- دستمزد تعیین سبب، علت، ارزیابی و تعیین میزان خسارت در کلیه رشته‌ها بر مبنای میزان خسارت تعیین شده طبق این ماده به اضافه پنجاه درصد می‌باشد.'
A11N5Text='ماده 11 تبصره ۵ (اصلاحی ۱۴۰۲/۰۸/۲۰)- دستمزد رسیدگی و ارزیابی قطعات یدکی، کالا و لوازم مستعمل، فرآورده‌های غذایی، دارویی و بهداشتی، کلیه ضایعات، ابزار آلات، اجزای ریزالکترونیک و مخابرات، در هر کار ارجاعی به صورت مستقل و یک جا طبق این ماده به اضافه پنجاه درصد می‌باشد. چنانچه اجزاء و قطعات فوق جزیی از کل مورد کارشناسی مانند خطوط تولید و انتقال، ماشین آلات و غیره باشد مشمول مقررات این تبصره نمی‌گردد.'
A11N6Text='ماده 11 تبصره ۶ (اصلاحی ۱۴۰۲/۰۸/۲۰)- در مواردی که موضوع کارشناسی توسط چند کارشناس از یک رشته کارشناسی انجام شود، از دستمزد هر کارشناس مبلغ سی درصد کسر می‌گردد. در این شرایط مبنای رعایت سقف تعرفه پس از کسر سی درصد خواهد بود و در صورتی که رسیدگی و ارزیابی توسط هیات کارشناسان با رشته‌های مختلف انجام شود، دستمزد کارشناس هر رشته به میزان سهم خود از ارزیابی، طبق تعرفه، جداگانه محاسبه‌ می‌شود.'
A11N7Text='ماده 11 تبصره ۷ (اصلاحی ۱۴۰۲/۰۸/۲۰)- ارزیابی ارزش دارایی‌های نامشهود مانند انواع برندها، صرفاً بر مبنای ارزش محاسبه شده، در کلیه رشته‌ها برابر این ماده به اضافه پنجاه درصد تعیین‌ می‌شود.'
A13Text='ماده ۱۳ (اصلاحی ۱۴۰۲/۰۸/۲۰)- دستمزد تعیین اجاره بهاء، برای کلیه رشته‌ها جهت هر واحد یا مجموعه مستقل تا اجاره ماهیانه پانزده میلیون ریال، مقطوعاً ‌۶.۰۰۰.۰۰۰ ریال و از پانزده میلیون و یک ریال تا پنجاه میلیون ریال ۲۰ درصد و از پنجاه میلیون و یک ریال تا یکصد میلیون ریال ۱۰ درصد، از یکصد میلیون ریال به بالا چهار درصد اضافه خواهد شد و حداکثر ششصد میلیون ریال می‌باشد.'

A45N2Text='ماده 45 تبصره 2: حق‌الزحمه کارشناسی نرم‌افزار کامپیوتر، مطابق ماده ۱۱ این تعرفه به اضافه ۵۰ درصد خواهد بود.'
A45N3Text='ماده 45 تبصره 3: دستمزد تشخیص اصالت اسناد دیجیتالی، امضای الکترونیکی، پیام‌های متنی، صوتی و تصویری در فضای مجازی، حملات سایبری و امنیت شبکه و عملکرد ماینرها حداقل ۱۰.۰۰۰.۰۰۰ ریال و حداکثر بر اساس ماده ۹ این تعرفه خواهد بود.'
A9Text='ماده ۹– در مواردی که برای بعضی از ارجاعات کارشناسی در این تعرفه دستمزد تعیین نشده باشد و نیز مواردی نظیر بررسی فنی و تکنولوژی سیستم‌ها و تعیین نقائص و سایر موارد حق‌الزحمه کارشناس با توجه به اهمیت و تخصصی بودن مورد به پیشنهاد کارشناس و موافقت مقام ارجاع‌کننده کانون یا مرکز تعیین می‌گردد و حداقل دستمزد ۶.۰۰۰.۰۰۰ ریال خواهد بود.'
A6Text='ماده ۶– درصورتی‌که اجرای قرار کارشناسی مستلزم عزیمت به خارج از شهر یا محل اقامت کارشناس باشد، تأمین وسیله ایاب و ذهاب و محل اقامت مناسب و غذا به عهده متقاضی بوده و علاوه بر دستمزد کارشناسی، فوق‌العاده مأموریت کارشناس برای هر روز مسافرت به مأخذ روزانه مبلغ ۳.۰۰۰.۰۰۰ ریال برای مأموریت داخل استان محل اقامت کارشناس و مبلغ ۶.۰۰۰.۰۰۰ ریال برای مأموریت خارج از استان محل اقامت کارشناس پرداخت خواهد شد. چنانچه متقاضی قادر به تأمین وسیله ایاب و ذهاب و اقامت نباشد و کارشناس برای انجام کارشناسی رأساً و به هزینه خود نسبت به تهیه موارد فوق‌الذکر اقدام نماید، علاوه بر دستمزد و فوق‌العاده مأموریت، هزینه‌های مربوط در وجه کارشناس پرداخت خواهد شد.\nتبصره ۱– درصورتی‌که انجام کارشناسی مستلزم عزیمت به خارج از کشور باشد، حق‌الزحمه انجام امور مربوط و کلیه هزینه‌های سفر و پرداخت فوق‌العاده روزانه هم‌ردیف مدیران کل به عهده متقاضی می‌باشد.\nتبصره ۲– چنانچه مبنای محاسبه حق‌الزحمه کارشناسی‌های خارج از کشور مطابق ضوابط این دستورالعمل پول سایر کشورها باشد، پس از تبدیل ارز به ریال بر اساس نرخ رسمی بانک مرکزی طبق جدول گروه مربوطه پرداخت خواهد شد.\nتبصره ۳– تأمین وسیله ایاب و ذهاب اجرای قرار کارشناسی درون شهرها به عهده متقاضی می‌باشد.'

class ExpertSalary(Ui_SalaryForm):
    def __init__(self,window):
        self.setupUi(window)
    
        self.totalAssessmentPrice_lineEdit.setValidator(QDoubleValidator())
        #self.totalAssessmentPrice_lineEdit.inputMask()
        self.monthlyRent_lineEdit.setValidator(QDoubleValidator())
        self.inStateNumMissionDays_lineEdit.setValidator(QDoubleValidator())
        self.outStateNumMissionDays_lineEdit.setValidator(QDoubleValidator())
        self.selAssessment_radioButton.setChecked(True)
        self.article13_frame.setDisabled(True)
        self.chooseArticle11Note3Type_comboBox.setDisabled(True)

        #Describe Selected Articles/Notes
        self.article11Note3_radioButton.clicked['bool'].connect(self.showArticleDesc)
        self.article11Note4_radioButton.clicked['bool'].connect(self.showArticleDesc)
        self.article11Note5_radioButton.clicked['bool'].connect(self.showArticleDesc)
        self.article11Note7_radioButton.clicked['bool'].connect(self.showArticleDesc)
        self.article11Note6_checkBox.clicked['bool'].connect(self.showArticleDesc)
        self.article45Note2_radioButton.clicked['bool'].connect(self.showArticleDesc)
        self.article45Note3_radioButton.clicked['bool'].connect(self.showArticleDesc)
        self.selAssessment_radioButton.clicked['bool'].connect(self.showArticleDesc)
        self.selectRent_radioButton.clicked['bool'].connect(self.showArticleDesc)
        self.selectMission_checkBox.clicked['bool'].connect(self.showArticleDesc)
        
        #config to evaluate salary on change selections
        #Article 11
        self.selAssessment_radioButton.clicked['bool'].connect(self.evalExpertSalary)
        self.article11Note3_radioButton.clicked['bool'].connect(self.evalExpertSalary)
        self.totalAssessmentPrice_lineEdit.textChanged.connect(self.evalExpertSalary)
        self.chooseArticle11Note3Type_comboBox.currentIndexChanged['int'].connect(self.evalExpertSalary)
        self.article11Note4_radioButton.clicked['bool'].connect(self.evalExpertSalary)
        self.article11Note5_radioButton.clicked['bool'].connect(self.evalExpertSalary)
        self.article11Note7_radioButton.clicked['bool'].connect(self.evalExpertSalary)
        self.article11Note6_checkBox.clicked['bool'].connect(self.evalExpertSalary)
    

        #Article 45
        self.article45Note2_radioButton.clicked['bool'].connect(self.evalExpertSalary)
        self.article45Note3_radioButton.clicked['bool'].connect(self.evalExpertSalary)

        #Article 13
        self.selectRent_radioButton.clicked['bool'].connect(self.evalExpertSalary)
        self.monthlyRent_lineEdit.textChanged.connect(self.evalExpertSalary)

        #Mission (Article 6)
        self.selectMission_checkBox.clicked['bool'].connect(self.evalExpertSalary)
        self.inStateNumMissionDays_lineEdit.textChanged.connect(self.evalExpertSalary)
        self.outStateNumMissionDays_lineEdit.textChanged.connect(self.evalExpertSalary)

 
    def showArticleDesc(self):
        articleDescText=''
        if self.article11Note3_radioButton.isChecked():
            articleDescText+=f'{A11N3Text}\n'
        if self.article11Note4_radioButton.isChecked():
            articleDescText+=f'{A11N4Text}\n'
        if self.article11Note5_radioButton.isChecked():
            articleDescText+=f'{A11N5Text}\n'
        if self.article11Note7_radioButton.isChecked():
            articleDescText+=f'{A11N7Text}\n'
        if self.article11Note6_checkBox.isChecked():
            articleDescText+=f'{A11N6Text}\n'
        if self.article45Note2_radioButton.isChecked():
            articleDescText+=f'{A45N2Text}\n'
        if self.article45Note3_radioButton.isChecked():
            articleDescText+=f'{A45N3Text}\n{A9Text}'
        if self.selectRent_radioButton.isChecked():
            articleDescText+=f'{A13Text}\n'
        if self.selectMission_checkBox.isChecked():
            articleDescText+=f'{A6Text}'
        
        self.selectedArticleNoteText_textEdit.setPlainText(articleDescText)
    
    def  evalExpertSalary(self):
        M11T3Value=0
        totalSalary=0
        if self.totalAssessmentPrice_lineEdit.text()=='' and self.selAssessment_radioButton.isChecked():
            self.evalSalary_lineEdit.setText('')
        elif self.selectRent_radioButton.isChecked() and self.monthlyRent_lineEdit.text()=='':
            self.evalSalary_lineEdit.setText('')
        elif self.selAssessment_radioButton.isChecked():
            #Article 11
            
            if self.article11Note3_radioButton.isChecked():
                if self.chooseArticle11Note3Type_comboBox.currentIndex()==0:
                    M11T3Value=0
                elif self.chooseArticle11Note3Type_comboBox.currentIndex()==1 or self.chooseArticle11Note3Type_comboBox.currentIndex()==2:
                    M11T3Value=50
                elif self.chooseArticle11Note3Type_comboBox.currentIndex()==3:
                    M11T3Value=100
            if self.totalAssessmentPrice_lineEdit.text()=='':
                evalPrice=0
            else:
                evalPrice=int(self.totalAssessmentPrice_lineEdit.text())
            totalSalary=evalArticle11(MabKar=evalPrice,
                          M11T3=M11T3Value,
                          M11T4=self.article11Note4_radioButton.isChecked().__int__,
                          M11T5=self.article11Note5_radioButton.isChecked().__int__,
                          M11T7=self.article11Note7_radioButton.isChecked().__int__,
                          M11T6=self.article11Note6_checkBox.isChecked().__int__)
            if totalSalary==-1:
                self.evalSalary_lineEdit.setText('اعمال ماده 11 تبصره 1')
                self.selectedArticleNoteText_textEdit.setPlainText(A11T1Text)
            else:
                if self.article45Note2_radioButton.isChecked():
                    totalSalary=evalArticle45(totalSalary,2)
                    totalSalary=int(totalSalary) #convert to int and round the float number
                    self.evalSalary_lineEdit.setText(f'{totalSalary:,}') #show salary by comma delimiter
                elif self.article45Note3_radioButton.isChecked():
                    totalSalary=evalArticle45(totalSalary,3)
                    self.evalSalary_lineEdit.setText('اعمال ماده 45 تبصره 3')
                    self.selectedArticleNoteText_textEdit.setPlainText(f'{A45N3Text}\n{A9Text}')
                else:   
                    totalSalary=int(totalSalary) #convert to int and round the float number
                    self.evalSalary_lineEdit.setText(f'{totalSalary:,}') #show salary by comma delimiter
        #Article 13
        elif self.selectRent_radioButton.isChecked():
            if self.monthlyRent_lineEdit.text()=='':
                evalPrice=0
            else:
                evalPrice=int(self.monthlyRent_lineEdit.text())
            totalSalary=evalArticle13(MabKar=evalPrice)
            totalSalary=int(totalSalary) #convert to int and round the float number
            self.evalSalary_lineEdit.setText(f'{int(totalSalary):,}') #show salary by comma delimiter
        #Evaluate Mission
        if self.inStateNumMissionDays_lineEdit.text()=='':
            self.inStateNumMissionDays_lineEdit.setText('0')
        if self.outStateNumMissionDays_lineEdit.text()=='':
            self.outStateNumMissionDays_lineEdit.setText('0')
        
        if (self.selAssessment_radioButton.isChecked() or self.selectRent_radioButton.isChecked())\
            and self.selectMission_checkBox.isChecked() and totalSalary>0:
            totalSalary+=evalMission(inStateDays=int(self.inStateNumMissionDays_lineEdit.text()),
                        outStateDays=int(self.outStateNumMissionDays_lineEdit.text()))
            self.evalSalary_lineEdit.setText(f'{int(totalSalary):,}') #show salary by comma delimiter
        elif self.article45Note3_radioButton.isChecked() and self.selectMission_checkBox.isChecked():
            totalSalary=evalMission(inStateDays=int(self.inStateNumMissionDays_lineEdit.text()),
                        outStateDays=int(self.outStateNumMissionDays_lineEdit.text()))
            self.evalSalary_lineEdit.setText(f'{int(totalSalary):,}') #show salary by comma delimiter




app = QtWidgets.QApplication(sys.argv)
SalaryForm = QtWidgets.QWidget()
ui = ExpertSalary(SalaryForm)
SalaryForm.show()
sys.exit(app.exec())