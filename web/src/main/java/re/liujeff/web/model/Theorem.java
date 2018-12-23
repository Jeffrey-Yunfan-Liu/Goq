package re.liujeff.web.model;

import lombok.Value;

import java.util.List;
import java.util.stream.Collectors;

@Value
public class Theorem {

    private final List<Hypothesis> results;
    private final List<Hypothesis> hypotheses;
    private final String name;
    private final String source;

    public String toPython(String delim) {
        List<String> results_strings = results.stream()
                .map(x -> x.toPython("+"))
                .collect(Collectors.toList());
        List<String> hypotheses_strings = hypotheses.stream()
                .map(x -> x.toPython("+"))
                .collect(Collectors.toList());
        return name+delim
                +results.size()+delim
                +String.join(delim, results_strings)+delim
                +hypotheses.size()+delim
                +String.join(delim, hypotheses_strings)+delim
                +source+delim;
    }

}
