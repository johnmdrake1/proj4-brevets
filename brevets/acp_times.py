"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """









    #TABLE DRIVEN DESIGN
    initialtime = arrow.get(brevet_start_time)

    #incdict = {">200": (200/34), ">400": (200/32), ">600": (200/30), ">1000": (400/28)}
    exdict = {200:5.883, 400:12.133, 600:18.8, 1000:33.083}
    inclist = [(200 / 34), (200 / 32), (200 / 30), (400 / 28)]
    #bradict = {"0-200": 34, "200-400": 32, "400-600": 30, "600-1000": 28, "1000-1300": 26}
    bralist = [34, 32, 30, 28, 26]
    increments = [200, 400, 600, 1000, 1300]
    total = 0
    totaldist = 0
    for i in range (len(increments)):
      if (increments[i] < control_dist_km):
        total = total + inclist[i]
        totaldist = increments[i]
      else:
        current = control_dist_km - totaldist
        toadd = current / bralist[i]
        total = total + toadd
        break

    



    newtime = initialtime.shift(hours=+total)

    if (control_dist_km > brevet_dist_km):
      newtime = initialtime.shift(hours=+(exdict[brevet_dist_km]))






      #OLD, MESSY, BUT FUNCTIONAL DESIGN BELOW:

    
    # first = 200 / 34
    # second = first + (200 / 32)
    # third = first + second + (200 / 30)
    # fourth = first + second + third + (400 / 28)




    # if(control_dist_km > 0 and control_dist_km < 200):
    #   open_time_raw = control_dist_km / 34
    #   newtime = initialtime.shift(hours=+open_time_raw)


    # elif(control_dist_km > 200 and control_dist_km < 400):
    #   bracket = control_dist_km - 200
    #   open_time_raw = first + (bracket / 32)
    #   newtime = initialtime.shift(hours=+open_time_raw)

    # elif(control_dist_km > 400 and control_dist_km < 600):
    #   bracket = control_dist_km - 400
    #   open_time_raw = first + second + (bracket / 30)
    #   newtime = initialtime.shift(hours=+open_time_raw)

    # elif(control_dist_km > 600 and control_dist_km < 1000):
    #   bracket = control_dist_km - 600
    #   open_time_raw = first + second + third + (bracket / 28)
    #   newtime = initialtime.shift(hours=+open_time_raw)

    # elif(control_dist_km > 1000 and control_dist_km < 1300):
    #   bracket = control_dist_km - 1000
    #   open_time_raw = first + second + third + fourth + (bracket / 26)
    #   newtime = initialtime.shift(hours=+open_time_raw)


    return newtime.isoformat()




    


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    initialtime = arrow.get(brevet_start_time)
    #MODIFIED TABLE DRIVEN DESIGN FROM open_time

    #incdict = {">200": (200/34), ">400": (200/32), ">600": (200/30), ">1000": (400/28)}
    exdict = {200:13.5, 400:27, 600:40, 1000:75}
    inclist = [(200 / 15), (200 / 15), (200 / 15), (400 / 11.428)]
    #bradict = {"0-200": 34, "200-400": 32, "400-600": 30, "600-1000": 28, "1000-1300": 26}
    bralist = [15, 15, 15, 11.428, 13.333]
    increments = [200, 400, 600, 1000, 1300]




    total = 0
    totaldist = 0

    for i in range (len(increments)):
      if (increments[i] < control_dist_km):
        total = total + inclist[i]
        totaldist = increments[i]
      else:
        current = control_dist_km - totaldist
        toadd = current / bralist[i]
        total = total + toadd
        break



    newtime = initialtime.shift(hours=+total)

    if (control_dist_km >= brevet_dist_km):
      newtime = initialtime.shift(hours=+exdict[brevet_dist_km])





    return newtime.isoformat()
