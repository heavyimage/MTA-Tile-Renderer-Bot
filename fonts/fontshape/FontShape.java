import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JComponent;
import javax.swing.JFrame;

class FontShape extends JComponent {
	
	private static final long serialVersionUID = 1L;
	private FontShapePanel panel;

	public static void main(String[] args) {
		new FontShape();
	}

	public FontShape() {
		JFrame frame = new JFrame();
		frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

		panel = new FontShapePanel();
		panel.setPreferredSize(new Dimension(500, 500));
		panel.setVisible(true);

		frame.getContentPane().add(panel, BorderLayout.CENTER);

		frame.pack();
		frame.setVisible(true);
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
	}
}
