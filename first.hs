module First where

import System.IO  
import Control.Monad

main :: IO ()
main = do  
        contents <- readFile "inputs/first.txt"
        print . part1 . map readInt . words $ contents
        print . part2 . map readInt . words $ contents

readInt :: String -> Int
readInt = read

part1 :: [Int] -> Int
part1 (x:xs) = head [x*y | x <- (x:xs), y <- (x:xs), x+y == 2020] 

part2 :: [Int] -> Int
part2 (x:xs) = head [x*y*z | x <- (x:xs), y <- (x:xs), z <- (x:xs), x+y+z == 2020] 
