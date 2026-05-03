import matplotlib.pyplot as plt
x=[2,2.5,3,3.5,4]
y=[0,1,2,3,4]
plt.plot(x,y)  #draw line from point to point
plt.show()
plt.plot(y,x,'o')   #just show points, don't draw line
plt.show()
plt.plot(y,x,marker='o') #draw lines with marks, marks can be emphasize by some special characters
plt.show()
plt.plot(x,y,'o:y')   # shortcut string notation parameter to specify the marker
plt.show()