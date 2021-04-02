from src import db


class Wallet(db.Model):
    __tablename__ = "wallet"
        
    date = db.Column("date", db.DateTime, primary_key=True)
    assets = db.Column("assets", db.JSON)
    dollar = db.Column("dollar", db.Float)


class WalletService:
    @classmethod
    def get_current_dollar(cls):
        session = db.Session()
        return session.query(Wallet.dollar).order_by(Wallet.date.desc()).first()

    @classmethod
    def get_current_crypto_all(cls):
        session = db.Session()
        return session.query(Wallet).order_by(Wallet.id.desc()).first()

    @classmethod
    def get_current_tether(cls):
        session = db.Session()
        return session.query(Wallet.usdt).order_by(Wallet.id.desc()).first()

    @classmethod
    def update_wallet(cls, ticker, amount, date, tether_amount):
        session = db.Session()
        current_wallet = session.query(Wallet).order_by(Wallet.id.desc()).first()
        session.expunge(current_wallet)
        make_transient(current_wallet)
        current_wallet.id += 1
        setattr(current_wallet, ticker, getattr(current_wallet, ticker) + amount)
        current_wallet.date = date
        current_wallet.usdt += tether_amount

        try:
            session.add(current_wallet)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def insert_wallet_data(cls, wallet):
        session = db.Session()
        try:
            session.add(wallet)
            session.commit()
        except Exception as e:
            session.rollback()
            # raise e
        finally:
            session.close()