namespace kkkkkkkkkkk
{
    public partial class P : Form
    {
        public P()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {
           
        }

        private void label6_Click(object sender, EventArgs e)
        {


        }

        private void broduct_SelectedIndexChanged(object sender, EventArgs e)
        {
            string broductt = broduct.Text;
            float totalll = 0;

            if (broductt == "koka")
            {
                totalll = 25;
            }
            else if (broductt == "boston")
            {
                totalll = 10;
            }
            else if (broductt == "cofree")
            {
                totalll = 2;
            }
            else if (broductt == "late")
            {
                totalll = 1;
            }

            price.Text = totalll.ToString();
        }
    }
}
