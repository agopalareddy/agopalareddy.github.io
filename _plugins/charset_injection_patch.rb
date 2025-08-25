# Dev-only patch to avoid NoMethodError in Jekyll 3.9.x + WEBrick 1.8.x
# When serving locally, some requests may call Jekyll::Commands::Serve::Servlet#conditionally_inject_charset
# with a nil headers object (observed when using hawkins liveserve). That triggers `undefined method `key?' for nil:NilClass`.
# This patch defensively guards the method so it no-ops when headers are nil, preventing noisy errors during local dev.

module CharsetInjectionPatch
  def self.apply
    # Ensure the target class exists
    return unless defined?(Jekyll) &&
                  defined?(Jekyll::Commands) &&
                  defined?(Jekyll::Commands::Serve) &&
                  defined?(Jekyll::Commands::Serve::Servlet)

    servlet = Jekyll::Commands::Serve::Servlet

    # Avoid applying twice
    return if servlet.instance_variable_defined?(:@_charset_patch_applied)

    mod = Module.new do
      # Keep arity flexible in case upstream changes
      def conditionally_inject_charset(*args)
        headers = args[0] if args.length >= 1
        type    = args[1] if args.length >= 2

        # If headers is nil or not hash-like, bail out and return original type
        return type if headers.nil? || !headers.respond_to?(:key?)

        # Otherwise, defer to the original implementation
        super(*args)
      rescue NoMethodError
        # If anything else goes wrong here, fail-safe by returning the type unchanged
        type
      end
    end

    servlet.prepend(mod)
    servlet.instance_variable_set(:@_charset_patch_applied, true)
  end
end

# Try to apply immediately (in case the class is already loaded)
begin
  CharsetInjectionPatch.apply
rescue StandardError => e
  warn "[charset_injection_patch] immediate apply failed: #{e.message}"
end

# Also apply after site init to catch cases where the class loads later
if defined?(Jekyll) && Jekyll.respond_to?(:Hooks)
  Jekyll::Hooks.register :site, :after_init do
    begin
      CharsetInjectionPatch.apply
    rescue StandardError => e
      Jekyll.logger.warn "charset_injection_patch", "apply on :after_init failed: #{e.message}"
    end
  end
end
