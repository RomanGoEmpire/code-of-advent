import gleam/int
import gleam/io
import gleam/list
import gleam/result
import gleam/string
import simplifile

fn extract_and_sort(items: List(List(String)), position) -> List(Int) {
  items
  |> list.map(fn(item) {
    position(item)
    |> result.unwrap("")
    |> int.parse()
    |> result.unwrap(0)
  })
  |> list.sort(int.compare)
}

pub fn day_one() {
  // Load file
  let data =
    case simplifile.read("src/1.txt") {
      Ok(text) -> text
      _ -> ""
    }
    |> string.split("\n")
    |> list.map(fn(line) { string.split(line, "   ") })

  // Part 1
  let first_col = extract_and_sort(data, list.first)
  let last_col = extract_and_sort(data, list.last)

  list.zip(first_col, last_col)
  |> list.map(fn(row) { int.absolute_value(row.0 - row.1) })
  |> list.fold(0, fn(count, e) { count + e })
  |> io.debug

  // Part 2
  list.unique(first_col)
  |> list.map(fn(value) {
    value * list.count(last_col, fn(second_value) { value == second_value })
  })
  |> list.fold(0, fn(count, e) { count + e })
  |> io.debug
}
