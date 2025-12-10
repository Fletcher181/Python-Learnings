package MiniTasks;

import java.util.Scanner;

public class ContinuityChecker {

    // Piecewise billing function (electricity pricing model)
    public static double f(double x) {
        if (0 <= x && x < 100) {
            // Tier 1: 10 pesos per kWh
            return 10 * x;
        } else if (100 <= x && x < 200) {
            // Tier 2: 8 pesos per kWh + fixed 200 pesos
            return 8 * x + 200;
        } else {
            // Tier 3: 7 pesos per kWh + fixed 300 pesos
            return 7 * x + 300;
        }
    }

    // Identify which formula / tier applies for a given x
    public static String getTierDescription(double x) {
        if (0 <= x && x < 100) {
            return "Tier 1: f(x) = 10x  (10 pesos per kWh)";
        } else if (100 <= x && x < 200) {
            return "Tier 2: f(x) = 8x + 200  (8 pesos per kWh + 200 pesos fixed charge)";
        } else {
            return "Tier 3: f(x) = 7x + 300  (7 pesos per kWh + 300 pesos fixed charge)";
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("=== Electricity Billing Continuity Checker ===");
        System.out.println("Piecewise billing function:");
        System.out.println("  0 <= x < 100    : f(x) = 10x");
        System.out.println("  100 <= x < 200  : f(x) = 8x + 200");
        System.out.println("  x >= 200        : f(x) = 7x + 300");
        System.out.println();
        System.out.print("Enter x (electricity usage in kWh) for continuity check: ");

        double c = sc.nextDouble();

        // Show which formula applies at x = c
        System.out.println();
        System.out.println("At x = " + c + " kWh:");
        System.out.println("Applied pricing tier: " + getTierDescription(c));

        // Small h to approximate left and right limits
        double h = 1e-5;

        double left = f(c - h);   // approximate left-hand limit
        double right = f(c + h);  // approximate right-hand limit
        double value = f(c);      // actual function value (bill)

        System.out.println();
        System.out.println("Approximate bill as usage approaches " + c + " kWh from the left:  " + left + " pesos");
        System.out.println("Approximate bill as usage approaches " + c + " kWh from the right: " + right + " pesos");
        System.out.println("Actual bill at exactly x = " + c + " kWh:                       " + value + " pesos");

        // Continuity test: LHL ≈ RHL ≈ f(c)
        double eps = 1e-3; // allow small floating-point differences
        boolean continuous = Math.abs(left - right) < eps && Math.abs(right - value) < eps;

        System.out.println();
        if (continuous) {
            System.out.println("Conclusion: The billing function is CONTINUOUS at x = " + c + " kWh.");
            System.out.println("There is no sudden jump in the bill at this usage level.");
        } else {
            System.out.println("Conclusion: The billing function is NOT CONTINUOUS at x = " + c + " kWh.");
            System.out.println("There is a billing jump (sudden change in the amount to pay) at this usage level.");
        }

        sc.close();
    }
}


//import java.util.Scanner;
//
//public class ContinuityChecker {
//
//    public static double f(double x) {
//        if (0 <= x && x < 100) return 10*x;
//        else if (100 <= x && x < 200) return 8*x + 200;
//        else return 7*x + 300;
//    }
//
//    public static void main(String[] args) {
//        Scanner sc = new Scanner(System.in);
//        System.out.print("Enter x for continuity check: ");
//        double c = sc.nextDouble();
//
//        double h = 1e-5;	
//        double left = f(c - h);
//        double right = f(c + h);
//        double value = f(c);
//
//        System.out.println("Left limit: " + left);
//        System.out.println("Right limit: " + right);
//        System.out.println("f(" + c + "): " + value);
//
//        if (Math.abs(left - right) < 1e-5 && Math.abs(right - value) < 1e-5)
//            System.out.println("Continuous at x = " + c);
//        else
//            System.out.println("NOT continuous at x = " + c);
//    }
//}
