from  main import Session,engine,User


local_session=Session(bind=engine)


user_to_delete=local_session.query(User).filter(User.username=="jonathan").first()

local_session.delete(user_to_delete)

local_session.commit()