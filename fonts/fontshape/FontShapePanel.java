import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Shape;
import java.util.List;
import javax.swing.JPanel;

class FontShapePanel extends JPanel {
	private static final long serialVersionUID = 1L;

	public void paintComponent(Graphics graphic) {
		super.paintComponent(graphic);
		Graphics2D g = (Graphics2D) graphic;

		// Write a String at 200px from the top.
		Shape shape = FontShapeHelper.getShape("Demo", new Font("Seriff",
				Font.PLAIN, 100), new Point(0, 200));

		// Draw a text preview
		g.draw(shape);

		// all Points
		List<Point> points = FontShapeHelper.getPoints(shape);

		// Output
		for (Point p : points) {
			System.out.println(p);
		}

		// Draw all points
		drawPoints(points, g);
	}

	public void drawPoints(List<Point> points, Graphics2D g) {
		for (Point p : points) {
			g.drawString(".", (int) p.getX(), (int) p.getY());
		}
	}
}