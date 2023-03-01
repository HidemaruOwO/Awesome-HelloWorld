proc main*() =
  type F = proc(): string {.noSideEffect.}
  func n(): F = return proc(): string = ""
  func H(): string = "H"
  func e(f: F): F = return proc(): string = f() & "e"
  func l(f: F): F = return proc(): string = f() & "l"
  func W(f: F): F = return proc(): string = f() & "W"
  func o(f: F): F = return proc(): string = f() & (if $f()[^1] == l(n())(): "o " else: "o")
  func r(f: F): F = return proc(): string = f() & "r"
  func d(f: F): string = f() & "d"

  echo H.e.l.l.o.W.o.r.l.d


when isMainModule:
  main()
