use std::fs;
use std::io::Read;

use std::time::Instant;

fn read_file(fp: String) -> Vec<i32> {

    let mut input_file = fs::File::open(fp).unwrap();

    let mut contents = String::new();

    input_file.read_to_string(&mut contents).unwrap();

    let mut v: Vec<i32> = Vec::new();

    for s in contents.lines(){

        v.push(s.parse::<i32>().unwrap());

    }

    return v;

}


fn main() {

    let mut before = Instant::now();

    let fp = String::from("input.txt");

    let input_numbers = read_file(fp);

    'outer: for number in input_numbers.iter(){

        for second_number in input_numbers.iter(){

            if second_number + number == 2020{

                println!("The result is: {}", number * second_number);

                break 'outer

            }
        }
    }

    println!("Stage 1, Elapsed time: {:.2?}", before.elapsed());
    
// Second part of the challange ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    before = Instant::now();

    'outer_stage_two: for number in input_numbers.iter(){

        for second_number in input_numbers.iter(){

            for third_number in input_numbers.iter(){

                if second_number + number + third_number == 2020{

                    println!("The result is: {}", number * second_number * third_number);
                    
                    break 'outer_stage_two

            }

 
            }
        }
    }
    println!("Stage 2, Elapsed time: {:.2?}", before.elapsed());




}
