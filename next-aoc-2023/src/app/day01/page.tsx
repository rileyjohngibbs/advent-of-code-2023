import { readFileSync } from "node:fs";
import SolutionStepper from "./SolutionStepper";

export default function Day01() {

    const inputLines = readFileSync("../inputs/01.txt", "utf-8").split("\n").filter(x => x)
    
    return <main className="flex flex-col font-mono">
        <SolutionStepper inputLines={inputLines} />
    </main>
}