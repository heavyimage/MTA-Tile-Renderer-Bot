import java.util.ArrayList;
import java.util.List;


public class Transformation {

	public static List<Point> translate(List<Point> points, int x, int y){
		List<Point> out = new ArrayList<Point>();
		
		for(Point p : points){
			out.add(new Point(p.getX() + x, p.getY() + y));
		}
		
		return out;
	}
}
