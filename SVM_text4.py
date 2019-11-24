
import pickle
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\2019-11-24_15-16-42.pickle" , "rb") as f1:
	data_list1 = pickle.load(f1)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\2019-11-24_15-19-09.pickle" , "rb") as f2:
	data_list2 = pickle.load(f2)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\2019-11-24_15-38-58.pickle" , "rb") as f3:
	data_list3 = pickle.load(f3)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\2019-11-24_15-26-11.pickle" , "rb") as f4:
	data_list4 = pickle.load(f4)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\2019-11-24_15-28-01.pickle" , "rb") as f5:
	data_list5 = pickle.load(f5)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\2019-11-24_15-31-45.pickle" , "rb") as f6:
	data_list6 = pickle.load(f6)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\2019-11-24_15-34-44.pickle" , "rb") as f7:
	data_list7 = pickle.load(f7)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\2019-11-24_15-36-41.pickle" , "rb") as f8:
	data_list8 = pickle.load(f8)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\0.pickle" , "rb") as f9:
	data_list9 = pickle.load(f9)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\35.pickle" , "rb") as f10:
	data_list10 = pickle.load(f10)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\40.pickle" , "rb") as f11:
	data_list11 = pickle.load(f11)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\50.pickle" , "rb") as f12:
	data_list12 = pickle.load(f12)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\90.pickle" , "rb") as f13:
	data_list13 = pickle.load(f13)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\130.pickle" , "rb") as f14:
	data_list14 = pickle.load(f14)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\155.pickle" , "rb") as f15:
	data_list15 = pickle.load(f15)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\195.pickle" , "rb") as f16:
	data_list16 = pickle.load(f16)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\123.pickle" , "rb") as f17:
	data_list17 = pickle.load(f17)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\98.pickle" , "rb") as f18:
	data_list18 = pickle.load(f18)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\17.pickle" , "rb") as f19:
	data_list19 = pickle.load(f19)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\77.pickle" , "rb") as f20:
	data_list20 = pickle.load(f20)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\178.pickle" , "rb") as f21:
	data_list21 = pickle.load(f21)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\7.pickle" , "rb") as f22:
	data_list22 = pickle.load(f22)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\22.pickle" , "rb") as f23:
	data_list23 = pickle.load(f23)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\63.pickle" , "rb") as f24:
	data_list24 = pickle.load(f24)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\111.pickle" , "rb") as f25:
	data_list25 = pickle.load(f25)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\142.pickle" , "rb") as f26:
	data_list26 = pickle.load(f26)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text4\\183.pickle" , "rb") as f27:
	data_list27 = pickle.load(f27)

Frame = [ ]
Status = [ ]
Ballposition = [ ]
Platformposition = [ ]
Bricks = [ ]
for i in range (0,len(data_list1)):
	Frame.append(data_list1[i].frame)
	Status.append(data_list1[i].status)
	Ballposition.append(data_list1[i].ball)
	Platformposition.append(data_list1[i].platform)
	Bricks.append(data_list1[i].bricks)
for i in range (0,len(data_list2)):
	Frame.append(data_list2[i].frame)
	Status.append(data_list2[i].status)
	Ballposition.append(data_list2[i].ball)
	Platformposition.append(data_list2[i].platform)
	Bricks.append(data_list2[i].bricks)
for i in range (0,len(data_list3)):
	Frame.append(data_list3[i].frame)
	Status.append(data_list3[i].status)
	Ballposition.append(data_list3[i].ball)
	Platformposition.append(data_list3[i].platform)
	Bricks.append(data_list3[i].bricks)
for i in range (0,len(data_list4)):
	Frame.append(data_list4[i].frame)
	Status.append(data_list4[i].status)
	Ballposition.append(data_list4[i].ball)
	Platformposition.append(data_list4[i].platform)
	Bricks.append(data_list4[i].bricks)
for i in range (0,len(data_list5)):
	Frame.append(data_list5[i].frame)
	Status.append(data_list5[i].status)
	Ballposition.append(data_list5[i].ball)
	Platformposition.append(data_list5[i].platform)
	Bricks.append(data_list5[i].bricks)
for i in range (0,len(data_list6)):
	Frame.append(data_list6[i].frame)
	Status.append(data_list6[i].status)
	Ballposition.append(data_list6[i].ball)
	Platformposition.append(data_list6[i].platform)
	Bricks.append(data_list6[i].bricks)
for i in range (0,len(data_list7)):
	Frame.append(data_list7[i].frame)
	Status.append(data_list7[i].status)
	Ballposition.append(data_list7[i].ball)
	Platformposition.append(data_list7[i].platform)
	Bricks.append(data_list7[i].bricks)
for i in range (0,len(data_list8)):
	Frame.append(data_list8[i].frame)
	Status.append(data_list8[i].status)
	Ballposition.append(data_list8[i].ball)
	Platformposition.append(data_list8[i].platform)
	Bricks.append(data_list8[i].bricks)
for i in range (0,len(data_list9)):
	Frame.append(data_list9[i].frame)
	Status.append(data_list9[i].status)
	Ballposition.append(data_list9[i].ball)
	Platformposition.append(data_list9[i].platform)
	Bricks.append(data_list9[i].bricks)
for i in range (0,len(data_list10)):
	Frame.append(data_list10[i].frame)
	Status.append(data_list10[i].status)
	Ballposition.append(data_list10[i].ball)
	Platformposition.append(data_list10[i].platform)
	Bricks.append(data_list10[i].bricks)
for i in range (0,len(data_list11)):
	Frame.append(data_list11[i].frame)
	Status.append(data_list11[i].status)
	Ballposition.append(data_list11[i].ball)
	Platformposition.append(data_list11[i].platform)
	Bricks.append(data_list11[i].bricks)
for i in range (0,len(data_list12)):
	Frame.append(data_list12[i].frame)
	Status.append(data_list12[i].status)
	Ballposition.append(data_list12[i].ball)
	Platformposition.append(data_list12[i].platform)
	Bricks.append(data_list12[i].bricks)
for i in range (0,len(data_list13)):
	Frame.append(data_list13[i].frame)
	Status.append(data_list13[i].status)
	Ballposition.append(data_list13[i].ball)
	Platformposition.append(data_list13[i].platform)
	Bricks.append(data_list13[i].bricks)
for i in range (0,len(data_list14)):
	Frame.append(data_list14[i].frame)
	Status.append(data_list14[i].status)
	Ballposition.append(data_list14[i].ball)
	Platformposition.append(data_list14[i].platform)
	Bricks.append(data_list14[i].bricks)
for i in range (0,len(data_list15)):
	Frame.append(data_list15[i].frame)
	Status.append(data_list15[i].status)
	Ballposition.append(data_list15[i].ball)
	Platformposition.append(data_list15[i].platform)
	Bricks.append(data_list15[i].bricks)
for i in range (0,len(data_list16)):
	Frame.append(data_list16[i].frame)
	Status.append(data_list16[i].status)
	Ballposition.append(data_list16[i].ball)
	Platformposition.append(data_list16[i].platform)
	Bricks.append(data_list16[i].bricks)
for i in range (0,len(data_list17)):
	Frame.append(data_list17[i].frame)
	Status.append(data_list17[i].status)
	Ballposition.append(data_list17[i].ball)
	Platformposition.append(data_list17[i].platform)
	Bricks.append(data_list17[i].bricks)
for i in range (0,len(data_list18)):
	Frame.append(data_list18[i].frame)
	Status.append(data_list18[i].status)
	Ballposition.append(data_list18[i].ball)
	Platformposition.append(data_list18[i].platform)
	Bricks.append(data_list18[i].bricks)
for i in range (0,len(data_list19)):
	Frame.append(data_list19[i].frame)
	Status.append(data_list19[i].status)
	Ballposition.append(data_list19[i].ball)
	Platformposition.append(data_list19[i].platform)
	Bricks.append(data_list19[i].bricks)
for i in range (0,len(data_list20)):
	Frame.append(data_list20[i].frame)
	Status.append(data_list20[i].status)
	Ballposition.append(data_list20[i].ball)
	Platformposition.append(data_list20[i].platform)
	Bricks.append(data_list20[i].bricks)
for i in range (0,len(data_list21)):
	Frame.append(data_list21[i].frame)
	Status.append(data_list21[i].status)
	Ballposition.append(data_list21[i].ball)
	Platformposition.append(data_list21[i].platform)
	Bricks.append(data_list21[i].bricks)
for i in range (0,len(data_list22)):
	Frame.append(data_list22[i].frame)
	Status.append(data_list22[i].status)
	Ballposition.append(data_list22[i].ball)
	Platformposition.append(data_list22[i].platform)
	Bricks.append(data_list22[i].bricks)
for i in range (0,len(data_list23)):
	Frame.append(data_list23[i].frame)
	Status.append(data_list23[i].status)
	Ballposition.append(data_list23[i].ball)
	Platformposition.append(data_list23[i].platform)
	Bricks.append(data_list23[i].bricks)
for i in range (0,len(data_list24)):
	Frame.append(data_list24[i].frame)
	Status.append(data_list24[i].status)
	Ballposition.append(data_list24[i].ball)
	Platformposition.append(data_list24[i].platform)
	Bricks.append(data_list24[i].bricks)
for i in range (0,len(data_list25)):
	Frame.append(data_list25[i].frame)
	Status.append(data_list25[i].status)
	Ballposition.append(data_list25[i].ball)
	Platformposition.append(data_list25[i].platform)
	Bricks.append(data_list25[i].bricks)
for i in range (0,len(data_list26)):
	Frame.append(data_list26[i].frame)
	Status.append(data_list26[i].status)
	Ballposition.append(data_list26[i].ball)
	Platformposition.append(data_list26[i].platform)
	Bricks.append(data_list26[i].bricks)
for i in range (0,len(data_list27)):
	Frame.append(data_list27[i].frame)
	Status.append(data_list27[i].status)
	Ballposition.append(data_list27[i].ball)
	Platformposition.append(data_list27[i].platform)
	Bricks.append(data_list27[i].bricks)



#----------------------------------------------------------------------------------------------------------------------------
import numpy as np
PlatX = np.array(Platformposition)[:,0][:,np.newaxis]
PlatX_next = PlatX[1:,:]
instruct = (PlatX_next - PlatX[0:len(PlatX_next),0][:, np.newaxis])/5

BallX=np.array(Ballposition)[:,0][:,np.newaxis]
BallX_next=BallX[1:,:]
vx=(BallX_next-BallX[0:len(BallX_next),0][:,np.newaxis])

BallY=np.array(Ballposition)[:,1][:,np.newaxis]
BallY_next=BallY[1:,:]
vy=(BallY_next-BallY[0:len(BallY_next),0][:,np.newaxis])

Ballarray = np.array(Ballposition[:-1])

x = np.hstack((Ballarray , PlatX[0:-1,0][:,np.newaxis],vx,vy))
#x = np.hstack((Ballarray , PlatX[0:-1,0][:,np.newaxis]))
y = instruct

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=41)

#----------------------------------------------------------------------------------------------------------------------------

from sklearn.svm import SVR

svr = SVR(gamma=0.001,C = 1,epsilon = 0.1,kernel = 'rbf')

svr.fit(x_train,y_train)  

y_forecast = svr.predict(x_test)

from sklearn.metrics import r2_score#R square


R2 = r2_score(y_test,y_forecast)
print('R2 = ',R2)

#----------------------------------------------------------------------------------------------------------------------------
#from sklearn.preprocessing import StandardScaler
#scaler = StandardScaler()
#scaler.fit(x_train)
#x_train_stdnorm = scaler.transform(x_train)
#knn.fit(x_train_stdnorm ,y_train)
#x_test_stdnorm = scaler.transform(x_test)
#yknn_aft_scaler = knn.predict(x_test_stdnorm)
#acc_knn_aft_scaler = accuracy_score(yknn_aft_scaler,y_test)


#----------------------------------------------------------------------------------------------------------------------------
filename = "C:\\Users\\user80710\\Downloads\\MLGame-master\\games\\arkanoid\\ml\\svr_text4.sav"
pickle.dump(svr , open(filename , 'wb'))