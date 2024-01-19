export class LineState {
    constructor(
        line: string,
        leftDigit: number | null = null,
        rightDigit: number | null = null,
        formedNumber: number | null = null
    ) {
        this.line = line
        this.leftDigit = leftDigit
        this.rightDigit = rightDigit
        this.formedNumber = formedNumber
    }
    line: string
    leftDigit: number | null
    rightDigit: number | null
    formedNumber: number | null
}

export class SolutionState {
    constructor(lineStates: LineState[], solution: number | null = null) {
        this.lineStates = lineStates
        this.solution = solution
    }
    lineStates: LineState[]
    solution: number | null
}
