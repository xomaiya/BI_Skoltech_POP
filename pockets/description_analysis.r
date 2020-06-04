r=read.table("~/pockets/pocket1_atm.pdb/mdpout_descriptors.txt",h=T)
ylim=c(0,1200)
plot(r[,"pock_volume"],ty='l',ylim=ylim,main="",xlab="",ylab="")
par(new=T)
plot(smooth.spline(r[,"pock_volume"],df=40),col="red",lwd=3,ylim=ylim,ty
     ="l",xlab="snapshot",ylab="volume")
