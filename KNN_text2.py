
import pickle
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_11-57-25.pickle" , "rb") as f1:
	data_list1 = pickle.load(f1)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-03-21.pickle" , "rb") as f2:
	data_list2 = pickle.load(f2)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-09-05.pickle" , "rb") as f3:
	data_list3 = pickle.load(f3)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-12-32.pickle" , "rb") as f4:
	data_list4 = pickle.load(f4)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-15-40.pickle" , "rb") as f5:
	data_list5 = pickle.load(f5)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-20-06.pickle" , "rb") as f6:
	data_list6 = pickle.load(f6)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-25-01.pickle" , "rb") as f7:
	data_list7 = pickle.load(f7)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-29-19.pickle" , "rb") as f8:
	data_list8 = pickle.load(f8)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-33-14.pickle" , "rb") as f9:
	data_list9 = pickle.load(f9)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-38-24.pickle" , "rb") as f10:
	data_list10 = pickle.load(f10)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-41-28.pickle" , "rb") as f11:
	data_list11 = pickle.load(f11)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-45-12.pickle" , "rb") as f12:
	data_list12 = pickle.load(f12)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-50-47.pickle" , "rb") as f13:
	data_list13 = pickle.load(f13)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-54-43.pickle" , "rb") as f14:
	data_list14 = pickle.load(f14)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-56-44.pickle" , "rb") as f15:
	data_list15 = pickle.load(f15)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_13-00-10.pickle" , "rb") as f16:
	data_list16 = pickle.load(f16)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_13-03-39.pickle" , "rb") as f17:
	data_list17 = pickle.load(f17)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_13-05-52.pickle" , "rb") as f18:
	data_list18 = pickle.load(f18)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_13-08-01.pickle" , "rb") as f19:
	data_list19 = pickle.load(f19)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_13-11-57.pickle" , "rb") as f20:
	data_list20 = pickle.load(f20)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_11-56-19.pickle" , "rb") as f21:
	data_list21 = pickle.load(f21)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-00-20.pickle" , "rb") as f22:
	data_list22 = pickle.load(f22)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-06-16.pickle" , "rb") as f23:
	data_list23 = pickle.load(f23)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-10-46.pickle" , "rb") as f24:
	data_list24 = pickle.load(f24)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-14-00.pickle" , "rb") as f25:
	data_list25 = pickle.load(f25)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-17-53.pickle" , "rb") as f26:
	data_list26 = pickle.load(f26)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-22-43.pickle" , "rb") as f27:
	data_list27 = pickle.load(f27)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-27-18.pickle" , "rb") as f28:
	data_list28 = pickle.load(f28)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-31-01.pickle" , "rb") as f29:
	data_list29 = pickle.load(f29)
with open ("C:\\Users\\user80710\\Downloads\\MLGame-master\\text2\\2019-10-07_12-35-53.pickle" , "rb") as f30:
	data_list30 = pickle.load(f30)





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
for i in range (0,len(data_list28)):
	Frame.append(data_list28[i].frame)
	Status.append(data_list28[i].status)
	Ballposition.append(data_list28[i].ball)
	Platformposition.append(data_list28[i].platform)
	Bricks.append(data_list28[i].bricks)
for i in range (0,len(data_list29)):
	Frame.append(data_list29[i].frame)
	Status.append(data_list29[i].status)
	Ballposition.append(data_list29[i].ball)
	Platformposition.append(data_list29[i].platform)
	Bricks.append(data_list29[i].bricks)
for i in range (0,len(data_list30)):
	Frame.append(data_list30[i].frame)
	Status.append(data_list30[i].status)
	Ballposition.append(data_list30[i].ball)
	Platformposition.append(data_list30[i].platform)
	Bricks.append(data_list30[i].bricks)



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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
knn = KNeighborsClassifier(n_neighbors = 5)

knn.fit(x_train,y_train)

yknn_bef_scaler = knn.predict(x_test)
acc_knn_bef_scaler = accuracy_score(yknn_bef_scaler, y_test)


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
filename = "C:\\Users\\user80710\\Downloads\\MLGame-master\\games\\arkanoid\\ml\\knn_text2.sav"
pickle.dump(knn , open(filename , 'wb'))
