namespace kkkkkkkkkkk
{
    partial class P
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            label4 = new Label();
            label5 = new Label();
            Total = new Label();
            broduct = new ComboBox();
            price = new TextBox();
            textBox2 = new TextBox();
            name = new TextBox();
            Quantity = new NumericUpDown();
            button1 = new Button();
            ((System.ComponentModel.ISupportInitialize)Quantity).BeginInit();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.BackColor = SystemColors.ControlLightLight;
            label1.ForeColor = Color.Red;
            label1.Location = new Point(646, 86);
            label1.Margin = new Padding(6, 0, 6, 0);
            label1.Name = "label1";
            label1.Size = new Size(123, 35);
            label1.TabIndex = 0;
            label1.Text = "broducct";
            label1.Click += label1_Click;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(409, 156);
            label2.Margin = new Padding(6, 0, 6, 0);
            label2.Name = "label2";
            label2.Size = new Size(51, 35);
            label2.TabIndex = 0;
            label2.Text = "N: ";
            label2.Click += label2_Click;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Location = new Point(329, 318);
            label3.Margin = new Padding(6, 0, 6, 0);
            label3.Name = "label3";
            label3.RightToLeft = RightToLeft.Yes;
            label3.Size = new Size(124, 35);
            label3.TabIndex = 0;
            label3.Text = "Quantity";
            label3.Click += label3_Click;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Location = new Point(271, 226);
            label4.Margin = new Padding(6, 0, 6, 0);
            label4.Name = "label4";
            label4.Size = new Size(180, 35);
            label4.TabIndex = 0;
            label4.Text = "brouct name:";
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Location = new Point(374, 402);
            label5.Margin = new Padding(6, 0, 6, 0);
            label5.Name = "label5";
            label5.Size = new Size(77, 35);
            label5.TabIndex = 0;
            label5.Text = "Price";
            // 
            // Total
            // 
            Total.AutoSize = true;
            Total.Location = new Point(361, 482);
            Total.Margin = new Padding(6, 0, 6, 0);
            Total.Name = "Total";
            Total.Size = new Size(79, 35);
            Total.TabIndex = 0;
            Total.Text = "Total";
            Total.Click += label6_Click;
            // 
            // broduct
            // 
            broduct.FormattingEnabled = true;
            broduct.Items.AddRange(new object[] { "koka", "late", "cofree", "boston" });
            broduct.Location = new Point(504, 218);
            broduct.Margin = new Padding(6, 5, 6, 5);
            broduct.Name = "broduct";
            broduct.Size = new Size(438, 43);
            broduct.TabIndex = 1;
            broduct.SelectedIndexChanged += broduct_SelectedIndexChanged;
            // 
            // price
            // 
            price.BorderStyle = BorderStyle.FixedSingle;
            price.Location = new Point(504, 396);
            price.Margin = new Padding(6, 5, 6, 5);
            price.Name = "price";
            price.Size = new Size(438, 41);
            price.TabIndex = 2;
            // 
            // textBox2
            // 
            textBox2.BorderStyle = BorderStyle.FixedSingle;
            textBox2.Location = new Point(504, 476);
            textBox2.Margin = new Padding(6, 5, 6, 5);
            textBox2.Name = "textBox2";
            textBox2.Size = new Size(438, 41);
            textBox2.TabIndex = 2;
            // 
            // name
            // 
            name.BorderStyle = BorderStyle.FixedSingle;
            name.Location = new Point(504, 150);
            name.Margin = new Padding(6, 5, 6, 5);
            name.Name = "name";
            name.Size = new Size(438, 41);
            name.TabIndex = 2;
            // 
            // Quantity
            // 
            Quantity.Location = new Point(504, 312);
            Quantity.Margin = new Padding(7, 5, 7, 5);
            Quantity.Name = "Quantity";
            Quantity.Size = new Size(438, 41);
            Quantity.TabIndex = 3;
            Quantity.Value = new decimal(new int[] { 2, 0, 0, 0 });
            // 
            // button1
            // 
            button1.Location = new Point(621, 525);
            button1.Name = "button1";
            button1.Size = new Size(182, 63);
            button1.TabIndex = 5;
            button1.Text = "Showe";
            button1.UseVisualStyleBackColor = true;
            // 
            // P
            // 
            AutoScaleDimensions = new SizeF(16F, 35F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = SystemColors.ButtonHighlight;
            ClientSize = new Size(1810, 901);
            Controls.Add(button1);
            Controls.Add(Quantity);
            Controls.Add(textBox2);
            Controls.Add(name);
            Controls.Add(price);
            Controls.Add(broduct);
            Controls.Add(Total);
            Controls.Add(label5);
            Controls.Add(label4);
            Controls.Add(label3);
            Controls.Add(label2);
            Controls.Add(label1);
            Font = new Font("Segoe UI Black", 15F, FontStyle.Bold | FontStyle.Italic, GraphicsUnit.Point, 0);
            Margin = new Padding(6, 5, 6, 5);
            Name = "P";
            Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)Quantity).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private Label label4;
        private Label label5;
        private Label Total;
        private ComboBox broduct;
        private TextBox price;
        private TextBox textBox2;
        private TextBox name;
        private NumericUpDown Quantity;
        private Button button1;
    }
}
