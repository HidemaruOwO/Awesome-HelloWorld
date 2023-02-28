defmodule ElixirLangTest do
  use ExUnit.Case
  doctest ElixirLang

  test "put Hello World" do
    assert :ok == ElixirLang.hello()
  end
end
