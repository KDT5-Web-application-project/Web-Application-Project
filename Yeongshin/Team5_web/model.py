from Team5_web import db

class Image_caption(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary, nullable=False)
    braille_image = db.Column(db.LargeBinary, nullable=False)
    caption = db.Column(db.Text, nullable=False)
    audio = db.Column(db.LargeBinary, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'Image(image={self.image}, caption="{self.caption}")'

class Sign_Caption(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary, nullable=False)
    result = db.Column(db.LargeBinary, nullable=False)
    sign = db.Column(db.LargeBinary, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    def __repr__(self):
        return f'Image(image={self.image}, sign="{self.sign}")'
class sign_caption(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.LargeBinary, nullable=False)
    braille_image = db.Column(db.LargeBinary, nullable=False)
    caption = db.Column(db.Text, nullable=False)
    audio = db.Column(db.LargeBinary, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'Image(image={self.image}, caption="{self.caption}")'

class Braille(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    braille_image = db.Column(db.LargeBinary, nullable=False)
    audio = db.Column(db.LargeBinary, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'Braille(braille={self.braille_image}, text="{self.text}")'

class Voice(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    voice = db.Column(db.LargeBinary, nullable=False)
    text = db.Column(db.Text, nullable=False)
    braile_image = db.Column(db.LargeBinary, nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return f'voice(voice={self.Voice})'