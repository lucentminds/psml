A simple script that allows for quick scripting in web pages like PHP, and ASP.

**<?py print 'Hello World!'; ?>**

Not perfect, but it is functional.

**IIS Installation:**

_This is assuming that your default python installation directory is 'C:\Python25\' and that you've place 'psml.py' in your 'Lib' directory._

Under your Web Site Properties, add a new Application Configuration:

  * Executable: "C:\Python25\python.exe" -u "C:\Python25\Lib\psml.py" "%s" "%s"
  * Extension: .psml
  * Select All Verbs, Script engine, & Check that file exists