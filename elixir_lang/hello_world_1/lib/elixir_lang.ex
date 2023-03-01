defmodule ElixirLang do
  @moduledoc """
  Hello World on Elixir
  """

  @doc """
  Show Hello world.

  ## Examples

      iex> ElixirLang.hello()
      :ok

  """

  def join(item) do
    list = []

    to_string(list) <> item
  end

  def hello do
    list = [
      "\u0048",
      "\u0065",
      "\u006c",
      "\u006c",
      "\u006f",
      "\u0020",
      "\u0057",
      "\u006f",
      "\u0072",
      "\u006c",
      "\u0064",
      "\u0021"
    ]

    Enum.join(list, "")
    |> IO.puts()
  end
end
