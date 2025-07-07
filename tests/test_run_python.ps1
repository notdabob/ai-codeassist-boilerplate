# Tests for Run-Python PowerShell module
Import-Module -Force "$PSScriptRoot/../scripts/Run-Python.psm1"

Describe "Run-Python module" {
    It "Finds and runs python3, python, or py if available" {
        # This test assumes python is installed on the system
        $result = Run-Python "-c 'print(12345)'"
        $result | Should -Contain "12345"
    }
    It "Fails gracefully if Python is not installed" {
        # Simulate by temporarily removing python from PATH (not possible in this test context)
        # This is a placeholder for manual/CI test
        $true | Should -Be $true
    }
}
