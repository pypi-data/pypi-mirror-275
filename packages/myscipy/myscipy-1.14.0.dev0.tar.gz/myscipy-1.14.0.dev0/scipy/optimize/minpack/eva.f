      recursive
     *double precision function eva(n,x)
      integer n
      double precision x(n)

c     **********
c
c     function eva
c
c     计算x对应的坐标，之后计算其弯曲半径
c
c     **********
      integer i, j, cnt, iter
      double precision ds, roc, tmpr, res, minr
      double precision p0(3), p1(3), p2(3), p3(3)
      double precision cx(n/7), cy(n/7), cz(n/7)
      double precision q1(n/7), q2(n/7), q3(n/7), q4(n/7)
      data one,zero /1.0d0,0.0d0/
c 
c     初始点坐标
c
      p0(1) = 0.1885
      p0(2) = 0.079
      p0(3) = 0.0795
c
c     ds：Δs
c     cnt：点的个数
c     res：evaluation值
c     minr：最小的弯曲半径
c
      ds = 0.012
      cnt = n / 7
      iter = 1
      res = 0
      minr = 0.036
c
c     把x里面的q1、q2、q3、q4存到对应的数组中
c
      
      do i = 1, n
        j = MOD(i, 7)
        if (j == 1) then
          q1(iter) = x(i)
        else if (j == 2) then
          q2(iter) = x(i)
        else if (j == 3) then
          q3(iter) = x(i)
        else if (j == 4) then
          q4(iter) = x(i)
        else if (j == 5) then
          iter = iter + 1
        end if
      end do
c
c     cx、cy、cz存储算出的坐标
c
      cx(1) = p0(1)
      cy(1) = p0(2)
      cz(1) = p0(3)

      do i = 2, cnt
        cx(i) = cx(i-1) + one / 3 * ds * (
     *  (2*q2(i-1) + q2(i)) * q4(i-1) + 
     *  (2*q2(i) + q2(i-1)) * q4(i) +
     *  (2*q1(i-1) + q1(i)) * q3(i-1) +
     *  (2*q1(i) + q1(i-1)) * q3(i)
     *  )

        cy(i) = cy(i-1) + one / 3 * ds * (
     *  (2*q3(i-1) + q3(i)) * q4(i-1) +
     *  (2*q3(i) + q3(i-1)) * q4(i) -
     *  (2*q1(i-1) + q1(i)) * q2(i-1) -
     *  (2*q1(i) + q1(i-1) * q2(i))
     *  )

        cz(i) = cz(i-1) + one / 3 * ds * (
     *  q1(i-1)**2 + q1(i-1)*q1(i) + q1(i)**2 +
     *  q4(i-1)**2 + q4(i-1)*q4(i) + q4(i)**2 -
     *  q2(i-1)**2 - q2(i-1)*q2(i) - q2(i)**2 -
     *  q3(i-1)**2 - q3(i-1)*q3(i) - q3(i)**2
     *  )
      enddo

c      print *, q1
c      print *, q2
c      print *, q3
c      print *, q4
      print *, cx
      print *, cy
      print *, cz

c
c     计算evaluation
c      
      do i = 2, cnt-1
        p1(1) = cx(i-1)
        p1(2) = cy(i-1)
        p1(3) = cz(i-1)

        p2(1) = cx(i)
        p2(2) = cy(i)
        p2(3) = cz(i)

        p3(1) = cx(i+1)
        p3(2) = cy(i+1)
        p3(3) = cz(i+1)

        tmpr = roc(p1, p2, p3)
        if (tmpr > minr) then
          res = res + 1
        end if
      end do

c      print *, roc(p0, p0, p0)

      eva = res
      print *, eva
      return
c
c     last card of function eva.
c
      end


      recursive
     *double precision function roc(p1,p2,p3)
      double precision p1(3),p2(3),p3(3)

c     **********
c
c     function roc
c
c     计算p1、p2、p3构成圆的半径
c
c     **********
      integer i
      double precision area, a, b, c
      double precision v1(3), v2(3), v3(3), cross(3)
      data eps,inf /1.0d-7,1.0d7/
      
      do i = 1, 3
        v1(i) = p1(i) - p2(i)
        v2(i) = p3(i) - p2(i)
        v3(i) = p3(i) - p1(i)
      end do

      cross(1) = v1(2)*v2(3)-v1(3)*v2(2)
      cross(2) = v1(3)*v2(1)-v1(1)*v2(3)
      cross(3) = v1(1)*v2(2)-v1(2)*v2(1)

c
c     三角形面积
c
      area = sqrt(cross(1)**2+cross(2)**2+cross(3)**2) / 2
c
c     三角形三边长
c
      a = sqrt(v1(1)**2 + v1(2)**2 + v1(3)**2)
      b = sqrt(v2(1)**2 + v2(2)**2 + v2(3)**2)
      c = sqrt(v3(1)**2 + v3(2)**2 + v3(3)**2)

      if (area .lt. eps) then
        roc = inf
      else 
        roc = a*b*c/(4*area)
      end if 
      
      return
c
c     last card of function roc.
c
      end

      program main

      integer n, i, j
      double precision res
      double precision x(35)
      double precision eva

      n = 35
      do i = 1, n
        j = MOD(i, 7)
        if (j == 1) then
          x(i) = -0.0701
        else if (j == 3) then
          x(i) = 0.0701
        else 
          x(i) = 0
        end if
      end do

      res = eva(n, x)

      end program
