using System;

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
            string bol = "";
            string[] args = Environment.GetCommandLineArgs();
            for (int i = 1; i < args.Length; i++)
            {
                if (System.IO.File.Exists(args[i]))
                {
                    bol = args[i];
                }
            }
            System.Diagnostics.Process p = new System.Diagnostics.Process();
            p.StartInfo.FileName = @"C:\Program Files\Wiimm\SZS\wimgt.exe";
            if (bol != "")
            {
                p.StartInfo.Arguments = "decode \"" + bol + "\" -o";
            }
            // p.StartInfo.UseShellExecute = false;
            // p.StartInfo.CreateNoWindow = false;
            // p.StartInfo.RedirectStandardOutput = true;
            // int len = lines[0].Length - lines[0].Split('\\')[lines[0].Split('\\').Length - 1].Length;
            // System.IO.Directory.SetCurrentDirectory(lines[0].Substring(0, len));
            // p.StartInfo.WorkingDirectory = lines[0].Substring(0, len);
            p.Start();
            p.WaitForExit();
            if (!System.IO.File.Exists(bol + ".png"))  // this heppens if wimgt.exe is not located on the C drive
            {
                string appdata = Environment.GetEnvironmentVariable("%programfiles%");
                if (System.IO.File.Exists(appdata + "\\Wiimm\\SZS\\wimgt.exe"))
                {

                    System.Diagnostics.Process q = new System.Diagnostics.Process();
                    q.StartInfo.FileName = appdata + "\\Wiimm\\SZS\\wimgt.exe";
                    if (bol != "")
                    {
                        p.StartInfo.Arguments = "decode \"" + bol + "\" -o";
                    }
                    // p.StartInfo.UseShellExecute = false;
                    // p.StartInfo.CreateNoWindow = false;
                    // p.StartInfo.RedirectStandardOutput = true;
                    // int len = lines[0].Length - lines[0].Split('\\')[lines[0].Split('\\').Length - 1].Length;
                    // System.IO.Directory.SetCurrentDirectory(lines[0].Substring(0, len));
                    // p.StartInfo.WorkingDirectory = lines[0].Substring(0, len);
                    q.Start();
                }
            }
            else
            {
                Console.WriteLine("wimgt.exe not recognised. Please install Wiimms SZS Tools to its default path (C:/Program Files/Wiimm/SZS) for this program to work.");
            }

        }
    }
}
