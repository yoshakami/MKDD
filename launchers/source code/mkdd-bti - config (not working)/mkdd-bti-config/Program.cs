using System;
using System.Runtime.CompilerServices;

namespace mkdd_bol_editor
{
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            string[] args = Environment.GetCommandLineArgs();
            string[] bti = new string[args.Length];
            string execPath = AppDomain.CurrentDomain.BaseDirectory;
            int j = 0;
            for (int i = 1; i < args.Length; i++)
            {
                if (System.IO.File.Exists(args[i]))
                {
                    bti[j] = args[i];
                    j++;
                }
            }
            if (!System.IO.File.Exists(execPath + "mkdd_bti.txt"))  // if the config file doesn't exists
            {
                string program_files = Environment.GetEnvironmentVariable("ProgramFiles");
                string[] lines = { "" };
                if (System.IO.File.Exists(program_files + "\\Wiimm\\SZS\\wimgt.exe"))
                {
                    lines[0] = program_files + "\\Wiimm\\SZS\\wimgt.exe";
                }
                else
                {
                    lines[0] = "\\Path\\To\\wimgt.exe";
                }
                System.IO.File.WriteAllLines(execPath + "mkdd_bti.txt", lines);
            }
            else
            {
                string[] lines = System.IO.File.ReadAllLines(execPath + "mkdd_bti.txt");  // each line of the config file is in the lines array
                if (lines.Length > 1)
                {
                    for (int i = 0; i < bti.Length; i++)
                    {
                        System.Diagnostics.Process p = new System.Diagnostics.Process();
                        p.StartInfo.FileName = lines[0];
                        p.StartInfo.Arguments = "decode \"" + bti[i] + "\" -o";
                        p.Start();
                    }
                }
            }
        }
    }
}
