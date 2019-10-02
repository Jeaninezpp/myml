function fout=charray(a,b,c)
%EXAMP Summary of this function goes here
%   Detailed explanation goes here
if nargin==1
    fout=a;
elseif nargin==2
	fout=a+b;
elseif nargin==3
    fout=(a*b*c)/2
end
