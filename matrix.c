#include<stdio.h>
int main()
{
  int a[4][4];
  int sumr1=0;
  int sumr2=0;
  int sumr3=0;
  int sumc1=0;
  int sumc2=0;
  int sumc3=0;
  int fsum=0;
  int i,j;
  for(i=0;i<3;i++)
    {
      for(j=0;j<3;j++)
        {
          scanf("%d\t",&a[i][j]);
        }
      printf("\n");
    }
  for(i=0;i<3;i++)
    {
      sumr1=sumr1+a[0][i];
    }
  a[0][3]=sumr1;
  for(i=0;i<3;i++)
    {
      sumr2=sumr2+a[1][i];
    }
  a[1][3]=sumr2;
  for(i=0;i<3;i++)
    {
      sumr3=sumr3+a[2][i];
    }
  a[2][3]=sumr3;
  for(j=0;j<3;j++)
    {
      sumc1=sumc1+a[j][0];
    }
  a[3][0]=sumc1;
  for(j=0;j<3;j++)
    {
      sumc2=sumc2+a[j][1];
    }
  a[3][1]=sumc2;
  for(j=0;j<3;j++)
    {
      sumc3=sumc3+a[j][2];
    }
  a[3][2]=sumc3;

  fsum=sumc1+sumc2+sumc3;
  printf("Fsum:%d\n",fsum);
  printf("Fsumr1:%d\n",sumr1);

}
