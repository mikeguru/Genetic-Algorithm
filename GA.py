__author__ = "Wen Jiang"

import math
import random
import csv

import matplotlib.pyplot as plt
import numpy as np
import quandl


def gda ( sbl="WIKI/TSLA" , st="2013-10-08" , ed="2017-10-08" , fid="Adj. Close" ):
    al = quandl.get ( sbl ,
                      authtoken='MgUeDFrhs9JjaA4gKzEx' )
    d = al.loc[ st:ed , fid ]

    return (d)


def gi ( min , max , n ):
    if (max <= min) or (n < 2) or (n > 10):
        return

    inc = int ( round ( (max - min) / (n + 1) ) )

    st = min
    ne = min + inc

    a = random.randint ( st , ne )
    b = random.randint ( ne + 1 , ne + (2 * inc) )

    if n == 2:
        ins = (a , b)
    elif n == 3:
        c = random.randint ( ne + (2 * inc) + 1 , max )
        ins = (a , b , c)
    elif n == 4:
        c = random.randint ( ne + (2 * inc) + 1 , ne + (3 * inc) )
        d = random.randint ( ne + (3 * inc) + 1 , max )
        ins = (a , b , c , d)
    elif n == 5:
        c = random.randint ( ne + (2 * inc) + 1 , ne + (3 * inc) )
        d = random.randint ( ne + (3 * inc) + 1 , ne + (4 * inc) )
        e = random.randint ( ne + (4 * inc) + 1 , max )
        ins = (a , b , c , d , e)
    elif n == 6:
        c = random.randint ( ne + (2 * inc) + 1 , ne + (3 * inc) )
        d = random.randint ( ne + (3 * inc) + 1 , ne + (4 * inc) )
        e = random.randint ( ne + (4 * inc) + 1 , ne + (5 * inc) )
        f = random.randint ( ne + (5 * inc) + 1 , max )
        ins = (a , b , c , d , e , f)
    elif n == 7:
        c = random.randint ( ne + (2 * inc) + 1 , ne + (3 * inc) )
        d = random.randint ( ne + (3 * inc) + 1 , ne + (4 * inc) )
        e = random.randint ( ne + (4 * inc) + 1 , ne + (5 * inc) )
        f = random.randint ( ne + (5 * inc) + 1 , ne + (6 * inc) )
        g = random.randint ( ne + (6 * inc) + 1 , max )
        ins = (a , b , c , d , e , f , g)
    elif n == 8:
        c = random.randint ( ne + (2 * inc) + 1 , ne + (3 * inc) )
        d = random.randint ( ne + (3 * inc) + 1 , ne + (4 * inc) )
        e = random.randint ( ne + (4 * inc) + 1 , ne + (5 * inc) )
        f = random.randint ( ne + (5 * inc) + 1 , ne + (6 * inc) )
        g = random.randint ( ne + (6 * inc) + 1 , ne + (7 * inc) )
        h = random.randint ( ne + (7 * inc) + 1 , max )
        ins = (a , b , c , d , e , f , g , h)
    elif n == 9:
        c = random.randint ( ne + (2 * inc) + 1 , ne + (3 * inc) )
        d = random.randint ( ne + (3 * inc) + 1 , ne + (4 * inc) )
        e = random.randint ( ne + (4 * inc) + 1 , ne + (5 * inc) )
        f = random.randint ( ne + (5 * inc) + 1 , ne + (6 * inc) )
        g = random.randint ( ne + (6 * inc) + 1 , ne + (7 * inc) )
        h = random.randint ( ne + (7 * inc) + 1 , ne + (8 * inc) )
        i = random.randint ( ne + (8 * inc) + 1 , max )
        ins = (a , b , c , d , e , f , g , h , i)
    else:
        c = random.randint ( ne + (2 * inc) + 1 , ne + (3 * inc) )
        d = random.randint ( ne + (3 * inc) + 1 , ne + (4 * inc) )
        e = random.randint ( ne + (4 * inc) + 1 , ne + (5 * inc) )
        f = random.randint ( ne + (5 * inc) + 1 , ne + (6 * inc) )
        g = random.randint ( ne + (6 * inc) + 1 , ne + (7 * inc) )
        h = random.randint ( ne + (7 * inc) + 1 , ne + (8 * inc) )
        i = random.randint ( ne + (8 * inc) + 1 , ne + (9 * inc) )
        j = random.randint ( ne + (9 * inc) + 1 , max )
        ins = (a , b , c , d , e , f , g , h , i , j)

    return ins


def cs ( a , allele , s , st , n ):
    if n == 3:
        if st[ s - 1 ] >= allele[ a ][ 0 ] and \
                        st[ s ] >= allele[ a ][ 1 ] and \
                        st[ s + 1 ] <= allele[ a ][ 2 ]:
            return True

    if n == 4:
        if (st[ s - 1 ] >= allele[ a ][ 0 ] or st[ s ] >= allele[ a ][ 1 ]) and \
                (st[ s ] >= allele[ a ][ 1 ] or st[ s + 1 ] <= allele[ a ][ 3 ]):
            return True

    if n == 5:
        if st[ s - 1 ] >= allele[ a ][ 0 ] and \
                (st[ s ] >= allele[ a ][ 1 ] or st[ s ] <= allele[ a ][ 2 ]) and \
                (st[ s + 1 ] >= allele[ a ][ 3 ] or st[ s + 1 ] <= allele[ a ][ 4 ]):
            return True

    if n == 6:
        if (st[ s - 1 ] >= allele[ a ][ 0 ] and st[ s - 1 ] < allele[ a ][ 1 ]) and \
                (st[ s ] >= allele[ a ][ 1 ] and st[ s ] < allele[ a ][ 2 ]) and \
                (st[ s + 1 ] >= allele[ a ][ 2 ] and st[ s + 1 ] < allele[ a ][ 3 ]) and \
                (st[ s + 2 ] >= allele[ a ][ 3 ] and st[ s + 2 ] < allele[ a ][ 4 ]) and \
                (st[ s + 3 ] >= allele[ a ][ 4 ] and st[ s + 3 ] <= allele[ a ][ 5 ]):
            return True


def gpo ( size , min , max , n ):
    C = [ ]
    for i in range ( 0 , size ):
        C.apped ( gi ( min , max , n ) )

    return C


def findYs ( ins , timeSeries , n ):
    mlt = [ ]
    mdt = {}

    for y in range ( len ( ins ) ):
        for x in range ( 1 , len ( timeSeries ) - 1 ):

            if cs ( y , ins , x , timeSeries , n ):
                mlt.apped ( timeSeries[ x ] )
                mdt[ ins[ y ] ] = mlt

        mlt = [ ]
    return mdt


def popfness ( po , yv , sta , sto ):
    popf = [ ]

    for i in range ( 0 , len ( po ) ):
        popf.apped ( fn ( po[ i ] , yv , sta , sto ) )
    return popf


def fn ( indl , yv , sta , sto , alpha=1 ):
    myfn = [ ]

    if len ( yv ) > 1:
        myfn.apped ( -math.log ( sta / sto - (alpha / len ( yv )) ) )
    else:
        myfn.apped ( 0 )
    return myfn


def fitfun ( yv , d ):
    sto = np.std ( d )
    i = 0
    pfl = [ ]
    cl = [ ]
    gpl = [ ]

    for k in yv.keys ( ):
        popf = popfness ( ins , yv , np.std ( yv[ k ] ) , sto )

        gpl.apped ( list ( yv[ k ] ) )

        cl.apped ( k )
        pfl.apped ( popf[ ++i ][ 0 ] )

    return pfl , cl , gpl


def cfn ( ins , d , ot ):
    yv = findYs ( ins , d , ot )

    pfl , cl , gpl = fitfun ( yv , d )

    return yv , pfl , cl , gpl


def rft ( pfl ):
    mii = pfl.index ( min ( pfl ) )
    mai = pfl.index ( max ( pfl ) )

    stl = sorted ( pfl )

    return mii , mai , stl


def sl ( gpl , mii ):
    if (len ( gpl ) == 4):
        slh = min (
            len ( i ) for i in
            [ gpl[ 0 ] , gpl[ 1 ] , gpl[ 2 ] , gpl[ 3 ] ] )
    elif (len ( gpl ) == 3):
        slh = min (
            len ( i ) for i in [ gpl[ 0 ] , gpl[ 1 ] , gpl[ 2 ] ] )
    elif (len ( gpl ) == 2):
        slh = min (
            len ( i ) for i in [ gpl[ 0 ] , gpl[ 1 ] ] )
    elif (len ( gpl ) == 1):
        slh = min (
            len ( i ) for i in [ gpl[ 0 ] ] )

    if (len ( gpl ) != 1):
        del gpl[ mii ]

        i = 0
        while (i < len ( gpl )):
            if (len ( gpl[ i ] ) > slh):
                del gpl[ i ][ -(len ( gpl[ i ] ) - slh): ]
            i = i + 1

    return gpl


def cro ( res ):
    ucr = .5
    cdo = [ ]

    k = 0

    while (k < len ( res ) - 1):
        if (k == 0):
            AL = list ( res[ k ] )
        else:
            AL = BL

        BL = list ( res[ k + 1 ] )

        for i in range ( len ( res[ k ] ) ):
            if ucr > random.random ( ):
                temp = AL[ i ]
                AL[ i ] = BL[ i ]
                BL[ i ] = temp

        cdo.apped ( AL )

        if (k == len ( res ) - 2):
            cdo.apped ( BL )

        k = k + 1

    return cdo


def mtt ( opg ):
    ctm = .01
    i = 0

    for p in opg:
        while (i < len ( p )):
            if ctm > random.random ( ):
                spot = random.randint ( 0 , len ( p ) - 1 )
                p[ spot ] = float ( "{0:.2f}".format ( random.uniform ( min ( p ) , max ( p ) ) ) )

            i = i + 1
        i = 0

    return opg


def scm ( gpl , mii ):
    clres = sl ( gpl , mii )

    opg = cro ( clres )

    nopg = mtt ( opg )

    return clres , opg , nopg


def roll ( data ):
    sr = data.rolling ( window=20 ).mean ( )
    lr = data.rolling ( window=50 ).mean ( )

    fig = plt.figure ( )
    ax = fig.add_subplot ( 1 , 1 , 1 )
    ax.plot ( data.index , data , label=str ( len ( data ) ) + ' dsp' )
    ax.plot ( sr.index , sr , label='20' )
    ax.plot ( lr.index , lr , label='50' )
    ax.set_xlabel ( 'time' )
    ax.set_ylabel ( 'value' )
    ax.leged ( )
    plt.show ( )


def gps ( uls , lcs , dfd ):
    lcr = lcs[ -30: ]

    fwp = [ ]

    min = min ( lcr[ -10: ] )
    max = max ( lcr[ -10: ] )
    lbk = (max - min) / 2

    for day in range ( dfd ):
        lbk = random.choice ( uls[ -30: ] )

        lbk = (random ( ) * (max - min)) + min;

        lpl = lcr[ p - lbk ]
        lpu = lpl + lbk
        ne = np.random.uniform ( lpl , lpu )
        fwp.apped ( ne )
        lcr.apped ( ne )
        lcr.pop ( 0 )

    return fwp


def fbt ( nopg , d , ot , pfl , gpl , mii ):
    counter = 0

    while (len ( nopg ) > 1):
        nws = [ ]
        for p in nopg:
            ip = int ( min ( p ) )
            ap = int ( max ( p ) )

            invi = gi ( ip , ap , 5 )
            nws.apped ( invi )

        yv , pfl , cl , gpl = cfn ( nws , d , ot )

        mii , mai , stl = rft ( pfl )

        clres , opg , nopg = scm ( gpl , mii )

    return clres , stl


if __name__ == '__main__':
    qsb = "WIKI/TSLA"
    d = gda ( qsb )

    wp = int ( min ( d ) )
    hp = int ( max ( d ) )

    ot = 5
    oi = 4

    ins = gpo ( oi , wp , hp , ot )

    yv , pfl , cl , gpl = cfn ( ins , d , ot )

    mii , mai , stl = rft ( pfl )

    clres , opg , nopg = scm ( gpl , mii )

    clres , stl = fbt ( nopg , d , ot , pfl , gpl , mii )
