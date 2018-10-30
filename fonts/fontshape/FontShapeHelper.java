import java.awt.Font;
import java.awt.Shape;
import java.awt.font.FontRenderContext;
import java.awt.font.TextLayout;
import java.awt.geom.AffineTransform;
import java.awt.geom.GeneralPath;
import java.awt.geom.PathIterator;
import java.util.ArrayList;
import java.util.List;

public class FontShapeHelper {

	public static Shape getShape(String text, Font font, Point from) {
		FontRenderContext context = new FontRenderContext(null, false, false);
	
		GeneralPath shape = new GeneralPath();
		TextLayout layout = new TextLayout(text, font, context);
	
		AffineTransform transform = AffineTransform.getTranslateInstance(
				from.getX(), from.getY());
	
		Shape outline = layout.getOutline(transform);
		shape.append(outline, true);
	
		return shape;
	}

	public static List<Point> getPoints(Shape shape) {
		List<Point> out = new ArrayList<Point>();
		PathIterator iterator = shape.getPathIterator(null);

		double[] coordinates = new double[6];
		double x = 0, y = 0;

		while (!iterator.isDone()) {

			double x1 = coordinates[0];
			double y1 = coordinates[1];

			double x2 = coordinates[2];
			double y2 = coordinates[3];

			double x3 = coordinates[4];
			double y3 = coordinates[5];

			switch (iterator.currentSegment(coordinates)) {
			case PathIterator.SEG_QUADTO:
				/*
				 * According to http://pfaedit.sourceforge.net/bezier.html Any
				 * quadratic spline can be expressed as a cubic (where the cubic
				 * term is zero). The end points of the cubic will be the same
				 * as the quadratic's.
				 * 
				 * x3 = x2 y3 = y2
				 * 
				 * The two control points for the cubic are:
				 * 
				 * x1 = x + 2/3 * (x1-x) y1 = y + 2/3 * (y1-y)
				 */

				x3 = x2;
				y3 = y2;

				x2 = x1 + 1 / 3f * (x2 - x1);
				y2 = y1 + 1 / 3f * (y2 - y1);

				x1 = x + 2 / 3f * (x1 - x);
				y1 = y + 2 / 3f * (y1 - y);

				out.add(new Point(x3, y3));

				x = x3;
				y = y3;
				break;

			case PathIterator.SEG_CUBICTO:
				out.add(new Point(x3, y3));
				x = x3;
				y = y3;
				break;
			case PathIterator.SEG_LINETO:
				out.add(new Point(x1, y1));
				x = x1;
				y = y1;
				break;
			case PathIterator.SEG_MOVETO:
				out.add(new Point(x1, y1));
				x = x1;
				y = y1;
				break;
			}
			iterator.next();
		}

		return out;
	}

}
