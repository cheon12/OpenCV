#include "opencv2/highgui/highgui.hpp"
using namespace cv;

int main()
{
Mat img;
img=imread('/home/cjy/Pictures/OpenCV/cat.png');
putText(img,"Hello bird",Point(60,50),FONT_HERSHEY_SIMPLEX,1,Scalar(255,0,0),1,CV_AA,false);
rectangle(img, Rect(30,25,350,30),Scalar(0,0,255));
cvnameWindow("Hello");
imshow("hello",img);
waitKey(5000);




return 0;
}