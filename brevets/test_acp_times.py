import acp_times as acp
import arrow
import nose

# print(acp.open_time(120,200,"2017-10-20T01:00"))
# print(acp.open_time(150,200,"2017-10-20T01:00"))
# print(acp.open_time(200,200,"2017-10-20T01:00"))
#print(acp.open_time(120,200,"2017-10-20T00:00"))
#print(acp.open_time(200, 200,"2017-10-20T00:00"))
# print(acp.open_time(203,400,"2017-10-20T14:30"))
# print(acp.open_time(270,400,"2017-10-20T14:30"))
# print(acp.open_time(350,400,"2017-10-20T14:30"))
# print(acp.open_time(410,400,"2017-10-20T14:30"))
#print(acp.open_time(120,200,"2017-10-20T00:00")


# print(acp.close_time(150,400,"2017-10-20T14:30"))
# print(acp.close_time(175,400,"2017-10-20T14:30"))
# print(acp.close_time(203,400,"2017-10-20T14:30"))
# print(acp.close_time(270,400,"2017-10-20T14:30"))
# print(acp.close_time(350,400,"2017-10-20T14:30"))
# print(acp.close_time(410,400,"2017-10-20T14:30"))
# print(acp.close_time(410,400,"2017-10-20T14:30"))


# def nearly(x,y):
#    """x is within 1% of y"""
#    xdh = arrow.get(x).format("YYYY-MM-DD-HH")
#    ydh = arrow.get(y).format("YYYY-MM-DD-HH")
#    x = int(arrow.get(x).format("mm")) / 60
#    y = int(arrow.get(y).format("mm")) / 60
   
#    return (xdh == ydh) and (1.01 * x >= y and 0.99 * x <= y)

def nearly(x, y):
	"""Based off Professor Michal Young's Piazza post.
	modified to work with dates. The function first makes sure the date of both arguments
	are exactly equal. It then concatenates the hours and minutes into a 4 digit integer, and checks
	to make sure they are very close(at most 1-3 minutes off)
	"""


	xd = arrow.get(x).format("YYYY-MM-DD")
	yd = arrow.get(y).format("YYYY-MM-DD")
	x = int(arrow.get(x).format("HHmm")) 
	y = int(arrow.get(y).format("HHmm")) 

	return (xd == yd) and (1.01 * x >= y and 0.99 * x <= y)




def test_lt_200():
	#Tests controls less than 200km for a 200km brevet starting at 00:00
	#15km control, 200km brevet
	assert nearly(acp.open_time(15,200,"2017-10-20T00:00"), "2017-10-20T00:26")
	assert nearly(acp.close_time(15,200,"2017-10-20T00:00"), "2017-10-20T01:00")
	#120km control, 200km brevet
	assert nearly(acp.open_time(120,200,"2017-10-20T00:00"), "2017-10-20T03:32")
	assert nearly(acp.close_time(120,200,"2017-10-20T00:00"), "2017-10-20T08:00")

def test_within_each_interval():
	"""Tests controls within each valid interval for brevet distances greater than 200km. Random distances used for each brevet length."""

	#400km brevet, 120km control
	assert nearly(acp.open_time(120,400,"2017-10-20T16:23"), "2017-10-20T19:55")
	assert nearly(acp.close_time(120,400,"2017-10-20T16:23"), "2017-10-21T00:23")

	#400km brevet, 260km control
	assert nearly(acp.open_time(260,400,"2017-10-20T16:23"), "2017-10-21T00:08")
	assert nearly(acp.close_time(260,400,"2017-10-20T16:23"), "2017-10-21T09:43")

	#400km brevet, 350km control
	assert nearly(acp.open_time(350,400,"2017-10-20T16:23"), "2017-10-21T02:57")
	assert nearly(acp.close_time(350,400,"2017-10-20T16:23"), "2017-10-21T15:43")

	#600km brevet, 130km control
	assert nearly(acp.open_time(130,600,"2017-10-20T16:23"), "2017-10-20T20:12")
	assert nearly(acp.close_time(130,600,"2017-10-20T16:23"), "2017-10-21T01:03")

	#600km brevet, 289km control
	assert nearly(acp.open_time(289,600,"2017-10-20T16:23"), "2017-10-21T01:03")
	assert nearly(acp.close_time(289,600,"2017-10-20T16:23"), "2017-10-21T11:39")

	#600km brevet, 343km control
	assert nearly(acp.open_time(343,600,"2017-10-20T16:23"), "2017-10-21T02:44")
	assert nearly(acp.close_time(343,600,"2017-10-20T16:23"), "2017-10-21T15:15")

	#600km brevet, 425km control
	assert nearly(acp.open_time(425,600,"2017-10-20T16:23"), "2017-10-21T05:21")
	assert nearly(acp.close_time(425,600,"2017-10-20T16:23"), "2017-10-21T20:43")

	#600km brevet, 555km control
	assert nearly(acp.open_time(555,600,"2017-10-20T16:23"), "2017-10-21T09:41")
	assert nearly(acp.close_time(555,600,"2017-10-20T16:23"), "2017-10-22T05:23")

	#1000km brevet, 167km control
	assert nearly(acp.open_time(167,1000,"2017-10-20T16:23"), "2017-10-20T21:18")
	assert nearly(acp.close_time(167,1000,"2017-10-20T16:23"), "2017-10-21T03:31")

	#1000km brevet, 203km control
	assert nearly(acp.open_time(203,1000,"2017-10-20T16:23"), "2017-10-20T22:22")
	assert nearly(acp.close_time(203,1000,"2017-10-20T16:23"), "2017-10-21T05:55")

	#1000km brevet, 366km control
	assert nearly(acp.open_time(366,1000,"2017-10-20T16:23"), "2017-10-21T03:27")
	assert nearly(acp.close_time(366,1000,"2017-10-20T16:23"), "2017-10-21T16:47")

	#1000km brevet, 413km control
	assert nearly(acp.open_time(413,1000,"2017-10-20T16:23"), "2017-10-21T04:57")
	assert nearly(acp.close_time(413,1000,"2017-10-20T16:23"), "2017-10-21T19:55")

	#1000km brevet, 556km control
	assert nearly(acp.open_time(556,1000,"2017-10-20T16:23"), "2017-10-21T09:43")
	assert nearly(acp.close_time(556,1000,"2017-10-20T16:23"), "2017-10-22T05:27")

	#1000km brevet, 667km control
	assert nearly(acp.open_time(667,1000,"2017-10-20T16:23"), "2017-10-21T13:35")
	assert nearly(acp.close_time(667,1000,"2017-10-20T16:23"), "2017-10-22T14:15")

	#1000km brevet, 703km control
	assert nearly(acp.open_time(703,1000,"2017-10-20T16:23"), "2017-10-21T14:52")
	assert nearly(acp.close_time(703,1000,"2017-10-20T16:23"), "2017-10-22T17:24")

	#1000km brevet, 845km control
	assert nearly(acp.open_time(845,1000,"2017-10-20T16:23"), "2017-10-21T19:56")
	assert nearly(acp.close_time(845,1000,"2017-10-20T16:23"), "2017-10-23T05:49")

	#1000km brevet, 980km control
	assert nearly(acp.open_time(980,1000,"2017-10-20T16:23"), "2017-10-22T00:45")
	assert nearly(acp.close_time(980,1000,"2017-10-20T16:23"), "2017-10-23T17:38")






def test_at_dists():
	#Tests control distances exactly at each possible brevet distance to make sure the calculator behaves according to rules.
	#varying times are used.

	#200km brevet, 200km control. Starts at 14:30

	assert nearly(acp.open_time(200,200,"2017-10-20T14:30"), "2017-10-20T20:23")
	assert nearly(acp.close_time(200,200,"2017-10-20T14:30"), "2017-10-21T04:00")

	

	#400km brevet, 400km control. Starts at 13:30

	assert nearly(acp.open_time(400,400,"2017-10-20T13:30"), "2017-10-21T01:38")
	assert nearly(acp.close_time(400,400,"2017-10-20T13:30"), "2017-10-21T16:30")


	#600km brevet, 600km control. Starts at 17:34

	assert nearly(acp.open_time(600,600,"2017-10-20T17:34"), "2017-10-21T12:22")
	assert nearly(acp.close_time(600,600,"2017-10-20T17:34"), "2017-10-22T09:34")

	#1000km brevet, 1000km control. Starts at 21:21

	assert nearly(acp.open_time(1000,1000,"2017-10-20T21:21"), "2017-10-22T06:26")
	assert nearly(acp.close_time(1000,1000,"2017-10-20T21:21"), "2017-10-24T00:21")



	
def test_near_dists():
	"""Tests control distances slightly over each possible total brevet distance to make sure calculator follows brevet rules and keeps open/close times
	at the same predetermined value when the control distance exceeds the brevet distance. Should be the same values as the previous tests, which were 
	controls placed exactly at the brevet distances themselves.
	"""

	#200km brevet, 206km control. Starts at 14:30
	assert nearly(acp.open_time(206,200,"2017-10-20T14:30"), "2017-10-20T20:23")
	assert nearly(acp.close_time(206,200,"2017-10-20T14:30"), "2017-10-21T04:00")

	#400km brevet, 407km control. Starts at 13:30
	assert nearly(acp.open_time(407,400,"2017-10-20T13:30"), "2017-10-21T01:38")
	assert nearly(acp.close_time(407,400,"2017-10-20T13:30"), "2017-10-21T16:30")

	#600km brevet, 605km control. Starts at 17:34
	assert nearly(acp.open_time(605,600,"2017-10-20T17:34"), "2017-10-21T12:22")
	assert nearly(acp.close_time(605,600,"2017-10-20T17:34"), "2017-10-22T09:34")

	#1000km brevet, 1005km control. Starts at 21:21

	assert nearly(acp.open_time(1005,1000,"2017-10-20T21:21"), "2017-10-22T06:26")
	assert nearly(acp.close_time(1005,1000,"2017-10-20T21:21"), "2017-10-24T00:21")

def test_near_irrelevant_dists():
	"""Tests controls near the same brevet distances as the previous function, but when these brevet distances are NOT the current one selected.
	The open and close times should not behave as if they were close to their total brevet distance in this test.
	"""

	#400km brevet, 206km control. Starts at 14:30
	assert nearly(acp.open_time(206,400,"2017-10-20T14:30"), "2017-10-20T20:34")
	assert nearly(acp.close_time(206,400,"2017-10-20T14:30"), "2017-10-21T04:14")

	#600km brevet, 407km control. Starts at 13:30
	assert nearly(acp.open_time(407,600,"2017-10-20T13:30"), "2017-10-21T01:52")
	assert nearly(acp.close_time(407,600,"2017-10-20T13:30"), "2017-10-21T16:38")

	#1000km brevet, 605km control. Starts at 17:34

	assert nearly(acp.open_time(605,1000,"2017-10-20T17:34"), "2017-10-21T12:33")
	assert nearly(acp.close_time(605,1000,"2017-10-20T17:34"), "2017-10-22T10:00")









	




