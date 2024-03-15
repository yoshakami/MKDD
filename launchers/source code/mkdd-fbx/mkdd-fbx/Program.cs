using System;
using System.Runtime.CompilerServices;

namespace mkdd_fbx
{
    internal static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            string bmd = "";
            string[] args = Environment.GetCommandLineArgs();
            string execPath = AppDomain.CurrentDomain.BaseDirectory;
            for (int i = 1; i < args.Length; i++)
            {
                if (System.IO.File.Exists(args[i]) && args[i].Substring(args[i].Length - 4) == ".fbx")
                {
                    bmd = args[i];
                }
            }
            bool materials = true;
            bool tex_headers = true;
            string SuperBMD_args = "\"" + bmd + "\"";
            string[] file = System.IO.Directory.GetFiles("./");
            for (int i = 0; i < file.Length && (materials || tex_headers); i++)
            {
                if (file[i].EndsWith("_materials.json") && materials)
                {
                    materials = false;
                    SuperBMD_args += " -m \"" + file[i] + "\"";
                }
                if (file[i].EndsWith("_tex_headers.json") && tex_headers)
                {
                    tex_headers = false;
                    SuperBMD_args += " -x \"" + file[i] + "\"";
                }
            }
            if (!System.IO.File.Exists(execPath + "mkdd_bmd.txt"))  // if the config file doesn't exists
            {
                string[] data = { execPath + "SuperBMD.exe" };
                System.IO.File.WriteAllLines(execPath + "mkdd_bmd.txt", data);

            }
            else  // config file exists
            {
                string[] lines = System.IO.File.ReadAllLines(execPath + "mkdd_bmd.txt");  // each line of the config file is in the lines array
                if (lines != null)
                {
                    System.Diagnostics.Process p = new System.Diagnostics.Process();
                    p.StartInfo.FileName = lines[0];
                    if (lines.Length > 1)
                    {
                        if (lines[1] != "")
                        {
                            SuperBMD_args += " " + lines[1];
                        }
                    }
                    if (bmd != "")
                    {
                        p.StartInfo.Arguments = SuperBMD_args;
                    }
                    p.Start();
                }
            }
        }
    }
}
