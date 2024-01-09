from django.db import models

class Customer(models.Model):
    class Meta:
        db_table_comment = "顧客マスタ"

    id   = models.AutoField (db_comment='ID', primary_key=True)
    mail = models.EmailField(db_comment='メールアドレス', unique=True, max_length=50 , blank = False, null = False)
    name = models.CharField (db_comment='会社名', max_length=50 , blank = False, null = False)
    post = models.CharField (db_comment='郵便番号', max_length=10, blank = False, null = False )
    addr = models.CharField (db_comment='住所', max_length=200, blank = True , null = True )
    tel  = models.CharField (db_comment='TEL', max_length=20 , blank = False, null = False)
    fax  = models.CharField (db_comment='FAX', max_length=20 , blank = True , null = True )
    note = models.TextField (db_comment='備考', blank = True , null = True )
    public_flag = models.BooleanField(db_comment='公開フラグ', default = False)
    delete_flag = models.BooleanField(db_comment='削除フラグ', default = False)
    created_at = models.DateTimeField(db_comment='作成日', auto_now=True)
    updated_at = models.DateTimeField(db_comment='更新日', auto_now_add=True)

    def __str__(self):
        return self.name