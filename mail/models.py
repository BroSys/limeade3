import crypt
from passlib.hash import sha512_crypt
from stdnet import odm
from advnet import fields

class Account(odm.StdModel):
	id       = fields.CompositeSymbolField('name', 'domain', seperator = '@', primary_key=True)
	domain   = fields.SortableSymbolField()
	name     = odm.SymbolField()
	password = odm.CharField()

	def __unicode__(self):
		return self.name + '@' + self.domain

	def set_password(self, password):
		self.password = sha512_crypt.encrypt(password)

	class Meta:
		ordering = 'id'


models = odm.Router('redis://localhost:6379')
models.register(Account)

	