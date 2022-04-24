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
            string obj = "";
            string[] args = Environment.GetCommandLineArgs();
            string execPath = AppDomain.CurrentDomain.BaseDirectory;
            for (int i = 1; i < args.Length; i++)
            {
                if (System.IO.File.Exists(args[i]) && args[i].Substring(args[i].Length - 4) == ".obj")
                {
                    obj = args[i];
                }
            }
            if (System.IO.File.Exists(execPath + "mkdd_obj.txt"))  // if the config file exists
            {
                string[] lines = System.IO.File.ReadAllLines(execPath + "mkdd_obj.txt");  // each line of the config file is in the lines array
                if (lines.Length > 1)
                {
                    System.Diagnostics.Process p = new System.Diagnostics.Process();
                    p.StartInfo.FileName = lines[0];
                    string launcher_args = '"' + lines[1] + "\"";
                    if (obj != "")
                    {
                        launcher_args += " \"" + obj + "\"";
                    }
                    if (System.IO.File.Exists(obj + "_sound.txt"))
                    {
                        launcher_args += " --soundfile \"" + obj + "_sound.txt\"";
                    }
                    p.StartInfo.Arguments = launcher_args;
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
                    string[] data = { dir[dir.Length - 1] + "\\python.exe", execPath + "mkdd-collision-creator.py" };
                    System.IO.File.WriteAllLines(execPath + "mkdd_obj.txt", data);
                }
                else
                {
                    string[] data = { "path to python", execPath + "mkdd-collision-creator.py" };
                    System.IO.File.WriteAllLines(execPath + "mkdd_obj.txt", data);
                }

            }
        }
    }
}
