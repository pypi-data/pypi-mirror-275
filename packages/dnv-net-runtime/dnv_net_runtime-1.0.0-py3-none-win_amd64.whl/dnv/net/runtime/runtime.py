class DotNetCore:
    def setup_clr_runtime(self):
        """
        Sets up the Common Language Runtime (CLR) for .NET Core.

        This method sets the environment variable 'DOTNET_ROOT' to specify the path where the .NET
        runtime is located.

        It also loads the CoreCLR runtime using Python.NET and sets it as the active runtime.
        """
        import os

        this_dir = os.path.abspath(os.path.dirname(__file__))
        dotnet_root = os.path.join(this_dir, ".net")

        from clr_loader import Runtime, get_coreclr
        from pythonnet import load, set_runtime

        # More on runtimeconfig @ https://learn.microsoft.com/en-us/dotnet/core/runtime-config/
        # Currently, it contains the .NET runtime version information which is updated from the
        # build pipeline
        config_runtime = True
        run_time: Runtime
        if config_runtime:
            runtime_config_path = os.path.join(this_dir, "runtimeconfig.json")
            if os.path.exists(runtime_config_path):
                run_time = get_coreclr(runtime_config=runtime_config_path, dotnet_root=dotnet_root)
                set_runtime(run_time)
            else:
                error = f"The file '{runtime_config_path}' does not exist."
                print(f"ERROR: {error}")
                raise FileNotFoundError(error)
        else:
            run_time = get_coreclr(dotnet_root=dotnet_root)

        load(run_time)

        import clr
        clr.AddReference("System.Runtime.InteropServices")
        from System.Runtime.InteropServices import RuntimeInformation
        runtime_info = RuntimeInformation
        print(f"INFO: The .NET Runtime Path '{dotnet_root}'")
        print(f"INFO: The .NET Runtime Version '{runtime_info.FrameworkDescription}'. "
              f"Runtime Identifier '{runtime_info.RuntimeIdentifier}'.")
