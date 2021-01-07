class Solution {
  
  def devvie(input: String): Int = {
    val position = setOut(input)
    comeBack(position)
  }
  
  def setOut(s: String, p: ((Int,Int),(Int,Int)) = ((0,0),(0,1))): ((Int,Int),(Int,Int)) = {
    s.headOption match {
      case Some('F') => setOut(s.tail, ((p._1._1 + p._2._1, p._1._2 + p._2._2), p._2))
      case Some('L') => setOut(s.tail, (p._1, (-p._2._2, p._2._1)))
      case Some('R') => setOut(s.tail, (p._1, (p._2._2, -p._2._1)))
      case Some(_)   => setOut(s.tail, p)
      case _ => p
    }
  }
  
  def comeBack(p: ((Int, Int),(Int, Int))): Int = {
    ((p._1._1).abs, (p._1._2).abs) match {
      case (0,0) => 0
      case (x, y) if (p._1._1 + p._2._1).abs < x || (p._1._2 + p._2._2).abs < y =>
      1 + comeBack(((p._1._1 + p._2._1, p._1._2 + p._2._2), p._2))
      case (x, y) if (p._1._1 - p._2._2).abs < x || (p._1._2 + p._2._1).abs < y =>
      1 + comeBack((p._1, (-p._2._2, p._2._1)))
      case _ =>
      1 + comeBack((p._1, (p._2._2, -p._2._1)))
    }
  }
  
}
