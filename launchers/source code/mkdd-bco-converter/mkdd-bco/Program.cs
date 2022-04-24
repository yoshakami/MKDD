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
            string execPath = AppDomain.CurrentDomain.BaseDirectory;
            for (int i = 1; i < args.Length; i++)
            {
                if (System.IO.File.Exists(args[i]) && args[i].Substring(args[i].Length - 4) == ".bco")
                {
                    bol = args[i];
                }
            }
            if (System.IO.File.Exists(execPath + "mkdd_bco.txt"))  // if the config file exists
            {
                string[] lines = System.IO.File.ReadAllLines(execPath + "mkdd_bco.txt");  // each line of the config file is in the lines array
                if (lines.Length > 1)
                {
                    System.Diagnostics.Process p = new System.Diagnostics.Process();
                    p.StartInfo.FileName = lines[0];
                    if (bol != "")
                    {
                        p.StartInfo.Arguments = '"' + lines[1] + "\" \"" + bol + "\"";
                    }
                    else
                    {
                        p.StartInfo.Arguments = lines[1];
                    }
                    // p.StartInfo.UseShellExecute = false;
                    // p.StartInfo.CreateNoWindow = false;
                    // p.StartInfo.RedirectStandardOutput = true;
                    // int len = lines[0].Length - lines[0].Split('\\')[lines[0].Split('\\').Length - 1].Length;
                    // System.IO.Directory.SetCurrentDirectory(lines[0].Substring(0, len));
                    // p.StartInfo.WorkingDirectory = lines[0].Substring(0, len);
                    p.Start();
                    /* p.WaitForExit();
                    while (!p.StandardOutput.EndOfStream)
                    {
                        string line = p.StandardOutput.ReadLine();
                        // do something with line
                        Console.WriteLine(line);
                    } */
                }
            }
            else
            {
                string appdata = Environment.GetEnvironmentVariable("LocalAppData");
                if (System.IO.Directory.Exists(appdata + "\\Programs\\Python"))
                {
                    string[] dir = System.IO.Directory.GetDirectories(appdata + "\\Programs\\Python");
                    string[] data = { dir[dir.Length - 1] + "\\python.exe", execPath + "mkdd-collision-reader.py" };
                    System.IO.File.WriteAllLines(execPath + "mkdd_bco.txt", data);
                }
                else
                {
                    string[] data = { "path to python", execPath + "mkdd-collision-reader.py" };
                    System.IO.File.WriteAllLines(execPath + "mkdd_bco.txt", data);
                }

            }
        }
    }
}
